
CREATE DATABASE dbSequenced;

--Primary Tables
CREATE TABLE tblReferenceSequences{
	RefSequenceID		integer CONSTRAINT pk_tblReferenceSequences PRIMARY KEY,
	ReferenceSequence 	varchar(MAX)
};

CREATE TABLE tblSequences{
	SequenceID			integer CONSTRAINT pk_tblSequences PRIMARY KEY,
	RefSequenceID 		integer REFERENCES tblReferenceSequences (RefSequenceID),
	RefDate				timestamp
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
	Region				varchar(MAX)
	--key value attributes
};

CREATE TABLE tblRAEvidence{
	RAEvidenceID		integer CONSTRAINT pk_tblRAEvidence PRIMARY KEY,
	Position 			integer,
	InsertPosition 		integer,
	RefBase 			char(1),
	NewBase 			char(1)
	-- Key Valued pairs
};

CREATE TABLE tblMCEvidence{
	MCEvidenceID 		integer CONSTRAINT pk_tblMCEvidence PRIMARY KEY,
	Start				integer,
	End					integer,
	StartRange			integer,
	EndRange			integer
	--Key Valued Pairs
};

CREATE TABLE tblJCEvidence{
	JCEvidenceID		integer CONSTRAINT pk_tblJCEvidence PRIMARY KEY,

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
CREATE TABLE tblMutationEvidence{
	MutationID 			integer REFERENCES tblMutations (MutationID),
	EvidenceID 			integer REFERENCES tblEvidence (EvidenceID)
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