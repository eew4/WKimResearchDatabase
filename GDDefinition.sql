
CREATE DATABASE dbSequenced;

CREATE TABLE tblReferenceSequences{
	SEQID		varchar(50) CONSTRAINT pk_tblReferenceSequences PRIMARY KEY
}

CREATE TABLE tblSNPMutation{
	SNPID		integer CONSTRAINT pk_tblSNPMutation PRIMARY KEY,
	SEQID		varchar(50),
	position	integer,
	newSeq		varchar(20)
};

CREATE TABLE tblSUBMutation{
	SUBID		integer CONSTRAINT pk_tblSUBMutation PRIMARY KEY,
	SEQID		varchar(50),
	position	integer,
	size		integer,
	newSeq		varchar(20)
};

CREATE TABLE tblDELMutation{
	DELID		integer CONSTRAINT pk_tblDELMutation PRIMARY KEY,
	SEQID		varchar(50),
	position	integer,
	size		integer
};

CREATE TABLE tblINSMutation{
	INSID		integer CONSTRAINT pk_tblINSMutation PRIMARY KEY,
	SEQID 		varchar(50),
	position 	integer,
	newSeq 		varchar(20)
};

CREATE TABLE tblMOBMutation{
	MOBID		integer CONSTRAINT pk_tblMOBMutation PRIMARY KEY,
	SEQID 		varchar(50),
	position 	integer,
	repeatName	varchar(50),
	strand		boolean,
	duplicationSize	integer
}

CREATE TABLE tblAMPMutation{
	AMPID		integer CONSTRAINT pk_tblAMPMutation PRIMARY KEY
}

CREATE TABLE tblCONMutation{
	CONID		integer CONSTRAINT pk_tblCONMutation PRIMARY KEY
}

CREATE TABLE tblINVMutation{
	INVID		integer CONSTRAINT pk_tblINVMutation PRIMARY KEY
}

CREATE TABLE tblRAEvidence{
	RAID 		integer CONSTRAINT pk_tblRAEvidence PRIMARY KEY
}

CREATE TABLE tblMCEvidence{
	MCID 		integer CONSTRAINT pk_tblMCEvidence	PRIMARY KEY
}

CREATE TABLE tblJCEvidence{
	JCID 		integer CONSTRAINT pk_tblJCEvidence PRIMARY KEY
}

CREATE TABLE tblUNEvidence{
	UNID 		integer CONSTRAINT pk_tblUNEvidence PRIMARY KEY
}

CREATE TABLE tblTSEQValidation{
	TSEQID 		integer CONSTRAINT pk_tblTSEQValidation PRIMARY KEY
}

CREATE TABLE tblPFLPValidation{
	PFLPID 		integer CONSTRAINT pk_tblPFLPValidation PRIMARY KEY
}

CREATE TABLE tblRFLPValidation{
	RFLPID 		integer CONSTRAINT pk_tblRFLPValidation PRIMARY KEY
}

CREATE TABLE tblPFGEValidation{
	PFGEID 		integer CONSTRAINT pk_tblPFGEValidation PRIMARY KEY
}

CREATE TABLE tblPHYLValidation{
	PHYLID 		integer CONSTRAINT pk_tblPHYLValidation PRIMARY KEY
}

CREATE TABLE tblCURAValidation{
	CURAID 		integer CONSTRAINT pk_tblCURAValidation PRIMARY KEY
}

CREATE TABLE tblMutationEvidence{
	MutationEvidenceID	integer CONSTRAINT pk_tblMutationEvidence PRIMARY KEY,
	SNPID				integer
}