CREATE TABLE Operadoras (
    id_operadora SERIAL PRIMARY KEY,
    registro_ans VARCHAR(20) NOT NULL UNIQUE,
    cnpj VARCHAR(20) NOT NULL UNIQUE,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100) NOT NULL,
    logradouro VARCHAR(255) NOT NULL,
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    uf CHAR(2) NOT NULL,
    cep VARCHAR(20) NOT NULL,
    ddd VARCHAR(2) ,
    telefone CHAR(20),
    fax VARCHAR(20),
    email VARCHAR(100),
    representante VARCHAR(100) NOT NULL,
    cargo_representante VARCHAR(100) NOT NULL,
    regiao_comercializacao VARCHAR(1),
    data_registro_ans DATE NOT NULL
);

CREATE TABLE PrimeiroT2023(
		id_conta SERIAL PRIMARY KEY,
		data_conta DATE NOT NULL,
		reg_ans VARCHAR(20) NOT NULL,
		conta_contabil VARCHAR(20) NOT NULL,
		description VARCHAR(100) NOT NULL ,
		vl_inicial INT NOT NULL,
		vl_final INT NOT NULL
);

CREATE TABLE SegundoT2023(
		id_conta SERIAL PRIMARY KEY,
		data_conta DATE NOT NULL,
		reg_ans VARCHAR(20) NOT NULL,
		conta_contabil VARCHAR(20) NOT NULL,
		description VARCHAR(100) NOT NULL,
		vl_inicial INT NOT NULL,
		vl_final INT NOT NULL
);

CREATE TABLE TerceiroT2023(
		id_conta SERIAL PRIMARY KEY,
		data_conta DATE NOT NULL,
		reg_ans VARCHAR(20) NOT NULL,
		conta_contabil VARCHAR(20) NOT NULL,
		description VARCHAR(100) NOT NULL,
		vl_inicial INT NOT NULL,
		vl_final INT NOT NULL

);

CREATE TABLE QuartoT2023(
		id_conta SERIAL PRIMARY KEY,
		data_conta DATE NOT NULL,
		reg_ans VARCHAR(20) NOT NULL,
		conta_contabil VARCHAR(20) NOT NULL,
		description VARCHAR(100) NOT NULL ,
		vl_inicial INT NOT NULL,
		vl_final INT NOT NULL

);

CREATE TABLE PrimeiroT2024(
	id_conta SERIAL PRIMARY KEY,
	data_conta DATE NOT NULL,
	reg_ans VARCHAR(20) NOT NULL,
	conta_contabil VARCHAR(20) NOT NULL,
	description VARCHAR(20) NOT NULL,
	vl_inicial INT NOT NULL,
	vl_final INT NOT NULL
);

CREATE TABLE SegundoT2024(
	id_conta SERIAL PRIMARY KEY,
	data_conta DATE NOT NULL,
	reg_ans VARCHAR(20) NOT NULL,
	conta_contabil VARCHAR(20) NOT NULL,
	description VARCHAR(20) NOT NULL,
	vl_inicial INT NOT NULL,
	vl_final INT NOT NULL
);

CREATE TABLE TerceiroT2024(
	id_conta SERIAL PRIMARY KEY,
	data_conta DATE NOT NULL,
	reg_ans VARCHAR(20) NOT NULL,
	conta_contabil VARCHAR(20) NOT NULL,
	description VARCHAR(20) NOT NULL,
	vl_inicial INT NOT NULL,
	vl_final INT NOT NULL
);

CREATE TABLE QuartoT2024(
	id_conta SERIAL PRIMARY KEY,
	data_conta DATE NOT NULL,
	reg_ans VARCHAR(20) NOT NULL,
	conta_contabil VARCHAR(20) NOT NULL,
	description VARCHAR(20) NOT NULL,
	vl_inicial INT NOT NULL,
	vl_final INT NOT NULL
);

