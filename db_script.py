import sqlite3 as sql

__author__ = 'Juan Manuel Bermúdez Cabrera'

con = sql.connect("resources/Pacientes.sqlite")

con.executescript("""
CREATE TABLE APPs(
    ID              INTEGER         NOT NULL,
    ID_PACIENTE      INTEGER         NOT NULL,
    HTA             BIT             NOT NULL,
    DM              SMALLINT        NOT NULL,
    CI              BIT             NOT NULL,
    fumador         SMALLINT        NOT NULL,
    HC              BIT             NOT NULL,
    HT              BIT             NOT NULL,
    otro            VARCHAR(200),
    IDiagnostico    VARCHAR(200),
    PRIMARY KEY (ID),
	FOREIGN KEY (ID_PACIENTE) REFERENCES Pacientes(ID)
)
;



--
-- TABLE: Arterias
--

CREATE TABLE Arterias(
    ID_TAC      INTEGER        NOT NULL,
    ID          INTEGER        NOT NULL,
    nombre      VARCHAR(20)    NOT NULL,
    lesiones    SMALLINT       DEFAULT 0 NOT NULL,
    volumen     FLOAT(10)      DEFAULT 0 NOT NULL,
    masa        FLOAT(10)      DEFAULT 0 NOT NULL,
    calcio      FLOAT(10)      DEFAULT 0 NOT NULL,
    PRIMARY KEY (ID),
	FOREIGN KEY (ID_TAC) REFERENCES TACs(ID)
)
;


--
-- TABLE: Complementarios
--

CREATE TABLE Complementarios(
    ID_PACIENTE       INTEGER      NOT NULL,
    ID               INTEGER      NOT NULL,
    Hb               FLOAT(10)    DEFAULT 0 NOT NULL,
    glicemia         FLOAT(10)    DEFAULT 0 NOT NULL,
    creatinina       FLOAT(10)    DEFAULT 0 NOT NULL,
    colesterol       FLOAT(10)    DEFAULT 0 NOT NULL,
    trigliceridos    FLOAT(10)    DEFAULT 0 NOT NULL,
    acido_urico      FLOAT(10)    DEFAULT 0 NOT NULL,
    PRIMARY KEY (ID),
	FOREIGN KEY (ID_PACIENTE) REFERENCES Pacientes(ID)
)
;



--
-- TABLE: Pacientes
--

CREATE TABLE Pacientes(
    ID                   INTEGER         NOT NULL,
    ID_PROVINCIA         INTEGER         NOT NULL,
    ID_APP               INTEGER,
    ID_COMPLEMENTARIO    INTEGER,
    ID_TAC               INTEGER,
    CI                   VARCHAR(11)     NOT NULL,
    nombre               VARCHAR(200)    NOT NULL,
    edad                 SMALLINT        NOT NULL,
    PRIMARY KEY (ID),
	FOREIGN KEY (ID_PROVINCIA) REFERENCES Provincias(ID)
)
;



--
-- TABLE: Provincias
--

CREATE TABLE Provincias(
    ID        INTEGER        NOT NULL,
    nombre    VARCHAR(20)    NOT NULL,
    PRIMARY KEY (ID)
)
;



--
-- TABLE: TACs
--

CREATE TABLE TACs(
    ID            INTEGER     NOT NULL,
    ID_PACIENTE    INTEGER     NOT NULL,
    angio_ct      CHAR(10)    DEFAULT "" NOT NULL,
    fecha         DATE        NOT NULL,
    PRIMARY KEY (ID),
	FOREIGN KEY (ID_PACIENTE) REFERENCES Pacientes(ID)
)
;
""")

con.close()
