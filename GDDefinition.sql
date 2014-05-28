
CREATE DATABASE dbSequenced;

--Primary Tables
CREATE TABLE tblReferenceSequences{
	RefSequenceID		integer CONSTRAINT pk_tblReferenceSequences PRIMARY KEY,
	ReferenceSequence 	varchar(126)
};

CREATE TABLE tblSequences{
	SequenceID			integer CONSTRAINT pk_tblSequences PRIMARY KEY,
	RefSequenceID 		integer REFERENCES tblReferenceSequences (RefSequenceID),
	RefDate				timestamp,
	--Correct Placement
	Generation			varchar(20)
};

CREATE TABLE tblFastqs{
	FastqID				integer CONSTRAINT pk_tblFastqs PRIMARY KEY,
	FastqFileName		varchar(50)
};

CREATE TABLE tblMutations{
	MutationID			integer CONSTRAINT pk_tblMutations PRIMARY KEY,
	MutationType		char(3) NOT NULL,
	Position			integer,
	Size				integer,
	NewSequence			varchar(50),
	RepeatName			varchar(50),
	Strand				boolean,
	DuplicationSize		integer,
	NewCopyNumber		integer,
	--double check for data type on Region
	Region				varchar(256),
	--key value pair attributes
	AANewSeq			varchar(20),
	AAPosition			integer,
	AARefSeq			varchar(20),
	CodonNewSeq			varchar(20),
	CodonNumber			integer,
	CodonPosition		integer,
	CodonRefSeq			varchar(20),
	Frequency			real,
	GeneList			varchar(20),
	GeneName			varchar(20),
	GenePosition		varchar(50),
	GeneProduct			varchar(250),
	GeneStrand			boolean,
	HTMLGeneName		varchar(50),
	LocusTag			varchar(20),
	SNPType				varchar(20),
	TranslationTable	integer
};

CREATE TABLE tblRAEvidence{
	RAEvidenceID		integer CONSTRAINT pk_tblRAEvidence PRIMARY KEY,
	Position 			integer,
	InsertPosition 		integer,
	RefBase 			char(1),
	NewBase 			char(1)
	-- Key Valued pairs
	AANewSeq			varchar(20),
	AAPosition			integer,
	AARefSeq			varchar(20),
	CodonNewSeq			varchar(20),
	CodonNumber			integer,
	CodonPosition		integer,
	CodonRefSeq			varchar(20),
	Frequency			real,
	GeneList			varchar(20),
	GeneName			varchar(20),
	GenePosition		varchar(50),
	GeneProduct			varchar(250),
	GeneStrand			boolean,
	HTMLGeneName		varchar(50),
	LocusTag			varchar(20),
	SNPType				varchar(20),
	TranslationTable	integer,
	BiasEValue			real,
	BiasPValue			real,
	FisherStrandPValue	real
};

CREATE TABLE tblMCEvidence{
	MCEvidenceID 		integer CONSTRAINT pk_tblMCEvidence PRIMARY KEY,
	Start				integer,
	End					integer,
	StartRange			integer,
	EndRange			integer
	--Key Valued Pairs
	GeneName			varchar(50),
	GeneProduct			varchar(100),
	HTMLGeneName 		varchar(50),
	LeftInsideCov		integer,
	LeftOutsideCov		integer,
	LocusTag 			varchar(20),
	RightInsideCov		integer,
	RightOutsideCov		integer
};

CREATE TABLE tblJCEvidence{
	JCEvidenceID			integer CONSTRAINT pk_tblJCEvidence PRIMARY KEY,
	Side1Position			integer,
	Side1Strand				boolean,
	Side2Position			integer,
	Side2Strand				boolean,
	Overlap 				integer,
	--Key Valude Pairs
	AlignmentOverlap		integer,
	CircularChromosome		integer,
	CoverageMinus			integer,
	CoveragePlus			integer,
	FlankingLeft			integer,
	FlankingRight			integer,
	Frequency				real,
	OverlapRegisters		integer,
	JunctionKey				varchar(150),
	MaxLeft					integer,
	MaxLeftMinus			integer,
	MaxLeftPlus				integer,
	MaxMinLeft				integer,
	MaxMinLeftMinus			integer,
	MaxMinLeftPlus			integer,
	MaxMinRight				integer,
	MaxMinRightMinus		integer,
	MaxMinRightPlus			integer,
	MaxPosHashScore			integer,
	MaxRight 				integer,
	MaxRightMinus 			integer,
	MaxRightPlus 			integer,
	NegLog10PosHashPValue	real,
	NewJunctionCoverage		real,
	NewJunctionFrequency	real,
	NewJunctionReadCount	integer,
	PosHashScore 			integer,
	Reject					varchar(5),
	ReadCountOffset			integer,
	Side1AnnotateKey		varchar(10),
	Side1Continution		integer,
	Side1Coverage			real,
	Side1Overlap			integer,
	Side1OverlapRegister	integer,
	Side1ReadCount			integer,
	Side1Redundant			boolean,
	Side2AnnotateKey		varchar(10),
	Side2Continution		integer,
	Side2Coverage			real,
	Side2Overlap			integer,
	Side2OverlapRegister	integer,
	Side2ReadCount			integer,
	Side2Redundant			boolean,
	TotalNonOverlapReads	integer,
	UniqueReadSequence		varchar(10)
};

CREATE TABLE tblUNEvidence{
	UNEvidenceID 		integer CONSTRAINT pk_tblUNEvidence PRIMARY KEY,
	Start 				integer,
	End 				integer
};

CREATE TABLE tblValidations{
	ValidationID		integer CONSTRAINT pk_tblValidations PRIMARY KEY,
	ValidationType		char(4)
};

--Bridge Tables
CREATE TABLE tblMutationRAEvidence{
	MutationID 			integer REFERENCES tblMutations (MutationID),
	RAEvidenceID 		integer REFERENCES tblEvidence (RAEvidenceID)
};

CREATE TABLE tblMutationMCEvidence{
	MutationID 			integer REFERENCES tblMutations (MutationID),
	MCEvidenceID 		integer REFERENCES tblEvidence (MCEvidenceID)
};

CREATE TABLE tblMutationJCEvidence{
	MutationID 			integer REFERENCES tblMutations (MutationID),
	JCEvidenceID 		integer REFERENCES tblEvidence (JCEvidenceID),
	JCSide				boolean
};

CREATE TABLE tblMutationUNEvidence{
	MutationID 			integer REFERENCES tblMutations (MutationID),
	UNEvidenceID 		integer REFERENCES tblEvidence (UNEvidenceID)
};

CREATE TABLE tblMutationValidation{
	MutationID 			integer REFERENCES tblMutations (MutationID),
	ValidationID		integer REFERENCES tblValidations (ValidationID)
}

CREATE TABLE tblMutationFastqs{
	FastqID 			integer REFERENCES tblFastqs (FastqID),
	MutationID 			integer REFERENCES tblMutations (MutationID)
};

CREATE TABLE tblFastqEvidence{
	FastqID 			integer REFERENCES tblFastqs (FastqID),
	EvidenceID 			integer REFERENCES tblEvidence (EvidenceID)
}