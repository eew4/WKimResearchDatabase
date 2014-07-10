#------------------------------------------------------------------------------
#File: transform.py
#Date: 
#Author:
#Parameters: 1) source gd file
#			 2) ouput filepath (future work)
#Issues: - record 11 in test file????
#		 - mkdir for all CSVs
#		 - database connectivity
#		 - check to be certain input is .gd
#------------------------------------------------------------------------------

import sys
import os
import recordDictionaries
from datetime import datetime

#input file parameter
gdInputFile = sys.argv[1] 
#outputPath = sys.argv[2]

fileDate = str(datetime.today())[:10]
folderPath = "CSVs"
if not os.path.exists(folderPath):
	os.makedirs(folderPath)
mutationTypes = ('SNP', 'SUB', 'DEL', 'INS', 'MOB', 'AMP', 'CON', 'INV')
mutationCSV = open(folderPath+'/mutation_'+fileDate+'.csv', 'wb')
raCSV = open(folderPath+'/ra_'+fileDate+'.csv', 'wb')
mcCSV = open(folderPath+'/mc_'+fileDate+'.csv', 'wb')
jcCSV = open(folderPath+'/jc_'+fileDate+'.csv', 'wb')
unCSV = open(folderPath+'/un_'+fileDate+'.csv', 'wb')

mutationColumns = []
raColumns = []
mcColumns = []
jcColumns = []
unColumns = []

#--------FUNCTIONS-------------------------------------------------------------
def Setup():
	#Setup the headers for each of the 5 CSV files
	mutationHeader = ['MutationID', 'MutationType', 'EvidenceID',
		'ParentID' ,'Position', 'Size', 
		'NewSequence', 'RepeatName', 'Strand', 'DuplicationSize', 
		'NewCopyNumber', 'Region', 'AANewSeq', 'AAPosition', 'AARefSeq', 
		'CodonNewSeq', 'CodonNumber', 'CodonPosition', 'CodonRefSeq', 
		'Frequency', 'GeneList', 'GeneName', 'GenePosition', 'GeneProdcut', 
		'GeneStrand', 'HTMLGeneName', 'LocusTag', 'SNPType', 'TranslationTable']
	raHeader = ['RAEvidenceID', 'ParentID','Position', 'InsertPosition', 'RefBase', 
		'NewBase', 'AANewSeq', 'AAPosition', 'AARefSeq', 'BiasEValue', 'BiasPValue',
		'CodonNewSeq', 'CodonNumber','CodonPosition', 'CodonRefSeq',
		'Deleted', 'FisherStrandPValue', 'Frequency', 'GeneList', 'GeneName', 'GenePosition', 'GeneProdcut',
		'GeneStrand', 'GenoTypeQuality', 'HTMLGeneName', 'KSQualityPValue',
		'Log10BaseLikelihood', 'Log10QualLikelihoodPositionModel',
		'Log10StrandLikelihoodPositionModel', 'LocusTag', 'Mixed', 'NewCov',
		'NewSeq', 'NoShow', 'PolymorphismChangedToConsensus','PolymorphismQuality', 'Quality', 
		'QualityPositionModel', 'RefCov', 'Reject', 'RefSeq', 'SNPType',
		'TotCov', 'TranslTable']
	mcHeader = ['MCEvidencID', 'ParentID','Start', 'End', 'StartRange', 'EndRange', 
		'GeneName', 'GeneProduct', 'HTMLGeneName', 'LeftInsideCov',
		'LeftOutsideCov', 'LocusTag', 'RightInsideCov', 'RightOutsideCov']
	jcHeader = ['JCEvidenceID', 'ParentID','Side1Position', 'Side1Strand', 'Side2Position',
		'Side2Strand', 'Overlap', 'AlignmentOverlap', 'CircularChromosome',
		'CoverageMinus', 'CoveragePlus', 'FlankingLeft', 'FlankingRight', 
		'Frequency', 'OverlapRegisters', 'JunctionKey', 'JunctionPossibleOverlapRegisters', 'KeyValue','MaxLeft',
		'MaxLeftMinus', 'MaxLeftPlus', 'MaxMinLeft', 'MaxMinLeftMinus',
		'MaxMinLeftPlus', 'MaxMinRight', 'MaxMinRightMinus', 'MaxMinRightPlus',
		'MaxPosHashScore', 'MaxRight', 'MaxRightMinus', 'MaxRightPlus', 
		'NegLog10PosHashPValue', 'NewJunctionCoverage', 'NewJunctionFrequency',
		'NewJunctionReadCount', 'PosHashScore', 'Reject', 'ReadCountOffset',
		'Side1AnnotateKey', 'Side1Continution', 'Side1Coverage', 'Side1PossibleOverlapRegisters','Side1Overlap',
		'Side1OverlapRegister', 'Side1ReadCount', 'Side1Redundant', 
		'Side2AnnotateKey', 'Side2Continution', 'Side2Coverage', 'Side2PossibleOverlapRegisters','Side2Overlap',
		'Side2OverlapRegister', 'Side2ReadCount', 'Side2Redundant',
		'TotalNonOverlapReads', 'UniqueReadSequence']
	unHeader = ['UNEvidenceID', 'ParentID', 'Start', 'End']
	writeRecord(mutationHeader, mutationCSV)
	writeRecord(raHeader, raCSV)
	writeRecord(mcHeader, mcCSV)
	writeRecord(jcHeader, jcCSV)
	writeRecord(unHeader, unCSV)

def mutationRecord(record):
	tabLoc1 = 0
	tabLoc2 = 0
	columnNum = 0
	columnString = ''
	readyForKeyValue = False
	mutationColumns.append(record[:3])
	#walks and parses out each column of tab delimited record
	while tabLoc1 >= 0 and tabLoc2 >= 0:
		tabLoc1 = record.find('\t', tabLoc2)
		tabLoc2 = record.find('\t', tabLoc1+1)
		columnString = record[tabLoc1+1:tabLoc2]
		#Key-value pairs
		if readyForKeyValue:
			newColumn = keyValueParse(columnString, 'mutation')
			while newColumn[0]+11 > len(mutationColumns)-1:
				mutationColumns.append('0')
			mutationColumns.append(newColumn[1])
		#consistent values
		elif columnNum < 4:
			mutationColumns.append(columnString)
		#begin mutation type specific parsing
		elif record[:3] == 'SNP' or record[:3] == 'INS':
			#last data point fill in
			mutationColumns.extend(('0',columnString,'0','0','0','0','0'))
			readyForKeyValue = True
		elif record[:3] == 'SUB':
			if columnNum == 4:
				mutationColumns.append(columnString)
			elif columnNum == 5:
				mutationColumns.extend((columnString,'0','0','0','0','0'))
				readyForKeyValue = True
		elif record[:3] == 'DEL' or record[:3] == 'INV':
			mutationColumns.append(columnString)
			readyForKeyValue = True
		elif record[:3] == 'MOB':
			if columnNum == 4:
				mutationColumns.extend(('0','0',columnString))
			elif columnNum == 5:
				mutationColumns.append(columnString)
			elif columnNum == 6:
				mutationColumns.extend((columnString,'0','0'))
				readyForKeyValue = True
		elif record[:3] == 'AMP':
			if columnNum == 4:
				mutationColumns.extend((columnString,'0','0','0','0'))
			elif columnNum == 5:
				mutationColumns.extend((columnString,'0'))
				readyForKeyValue = True
		elif record[:3] == 'CON':
			if columnNum == 4:
				mutationColumns.extend((columnString,'0','0','0','0','0'))
			elif columnNum == 5:
				mutationColumns.append(columnString)
				readyForKeyValue = True
		columnNum +=1
	#flip first two indices
	temp = mutationColumns[1]
	mutationColumns[1] = mutationColumns[0]
	mutationColumns[0] = temp
	mutationColumns[2].replace(",","/")
	#write record to file
	writeRecord(mutationColumns, mutationCSV)
	del mutationColumns[0:len(mutationColumns)]

#read and write RA Evidence records
def raRecord(record):
	tabLoc1 = 0
	tabLoc2 = 0
	columnNum = 0
	columnString = ''
	readyForKeyValue = False
	#walks and parses out each column of tab delimited record
	while tabLoc1 >= 0 and tabLoc2 >= 0:
		tabLoc1 = record.find('\t', tabLoc2)
		tabLoc2 = record.find('\t', tabLoc1+1)
		columnString = record[tabLoc1+1:tabLoc2]
		if readyForKeyValue:
			newColumn = keyValueParse(columnString, 'RA')
			while newColumn[0]+5 > len(raColumns)-1:
				raColumns.append('0')
			raColumns.append(newColumn[1])
		elif columnNum == 1:
			pass
		elif columnNum < 6:
			raColumns.append(columnString)
		elif columnNum == 6:
			raColumns.append(columnString)
			readyForKeyValue = True
		columnNum += 1
	writeRecord(raColumns, raCSV)
	del raColumns[0:len(raColumns)]

#!! similar number of non key valued pairs to RA may look at combining
def mcRecord(record):
	tabLoc1 = 0
	tabLoc2 = 0
	columnNum = 0
	columnString = ''
	readyForKeyValue = False
	#walks and parses out each column of tab delimited record
	while tabLoc1 >= 0 and tabLoc2 >= 0:
		tabLoc1 = record.find('\t', tabLoc2)
		tabLoc2 = record.find('\t', tabLoc1+1)
		columnString = record[tabLoc1+1:tabLoc2]
		if readyForKeyValue:
			newColumn = keyValueParse(columnString, 'MC')
			while newColumn[0]+5 > len(mcColumns)-1:
				mcColumns.append('0')
			mcColumns.append(newColumn[1])
		elif columnNum == 1:
			pass
		elif columnNum < 6:
			mcColumns.append(columnString)
		elif columnNum == 6:
			mcColumns.append(columnString)
			readyForKeyValue = True
		columnNum += 1
	writeRecord(mcColumns, mcCSV)
	del mcColumns[0:len(mcColumns)]

def jcRecord(record):
	tabLoc1 = 0
	tabLoc2 = 0
	columnNum = 0
	columnString = ''
	readyForKeyValue = False
	#walks and parses out each column of tab delimited record
	while tabLoc1 >= 0 and tabLoc2 >= 0:
		tabLoc1 = record.find('\t', tabLoc2)
		tabLoc2 = record.find('\t', tabLoc1+1)
		columnString = record[tabLoc1+1:tabLoc2]
		if readyForKeyValue:
			newColumn = keyValueParse(columnString, 'JC')
			while newColumn[0]+5 > len(jcColumns)-1:
				jcColumns.append('0')
			jcColumns.append(newColumn[1])
		elif columnNum == 1:
			pass
		elif columnNum < 8:
			jcColumns.append(columnString)
		elif columnNum == 8:
			jcColumns.append(columnString)
			readyForKeyValue = True
		columnNum += 1
	writeRecord(jcColumns, jcCSV)
	del jcColumns[0:len(jcColumns)]

def unRecord(record):
	tabLoc1 = 0
	tabLoc2 = 0
	columnNum = 0
	columnString = ''
	readyForKeyValue = False
	#walks and parses out each column of tab delimited record
	while tabLoc1 >= 0 and tabLoc2 >= 0:
		tabLoc1 = record.find('\t', tabLoc2)
		tabLoc2 = record.find('\t', tabLoc1+1)
		columnString = record[tabLoc1+1:tabLoc2]
		if columnNum == 1:
			pass
		else:
			unColumns.append(columnString)
		columnNum += 1
	writeRecord(unColumns, unCSV)
	del unColumns[0:len(unColumns)]

#unused as of yet (function before elegance)
# def moveByTab(tab1, tab2, record):
# 	returnValue = []
# 	returnValue.extend((record.find('\t', tab2), record.find('\t', tab1 + 1)))
# 	return returnValue

def keyValueParse(stringVar, valueType):
	returnValue = []
	if valueType == 'mutation':
		returnValue.append(recordDictionaries.mutationKeyValue(stringVar[:stringVar.find('=')]))
	elif valueType == 'RA':
		returnValue.append(recordDictionaries.RAKeyValue(stringVar[:stringVar.find('=')]))
	elif valueType == 'MC':
		returnValue.append(recordDictionaries.MCKeyValue(stringVar[:stringVar.find('=')]))
	elif valueType == 'JC':
		returnValue.append(recordDictionaries.JCKeyValue(stringVar[:stringVar.find('=')]))
	returnValue.append(stringVar[stringVar.find('=')+1:])
	return returnValue

def writeRecord(record, targetFile):
	for column in record:
		#Dealing with commas in fields for truer CSV output
		if column.find(',') > 0:
			commaLoc = column.find(',')
			column = column[:commaLoc] + '/' + column[commaLoc+1:]
		#Write to file
		targetFile.write(column)
		#CSV except for last spot
		if column != record[len(record)-1]:
			targetFile.write(',')
	targetFile.write('\n')

#--------RUNNING---------------------------------------------------------------
Setup()
fileInput = open(gdInputFile, "r")
for line in fileInput.readlines():
	if line[:3] in mutationTypes:
		mutationRecord(line)
	elif line[:2] == "RA":
		raRecord(line)
	elif line[:2] == "MC":
		mcRecord(line)
	elif line[:2] == "JC":
		jcRecord(line)
	elif line[:2] == "UN":
		unRecord(line)

