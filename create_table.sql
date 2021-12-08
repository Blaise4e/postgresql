-- Create table 

begin transaction;

CREATE TABLE lotissement (
    id SERIAL,
    id_lot VARCHAR,
    nb_piece int,
    typologie VARCHAR (50),
    prix_tva_reduit FLOAT(6) NULL,
    prix_tva_normal FLOAT(6),
    prix_ht FLOAT(6),
    prix_m_ht FLOAT(5),
    prix_m_ttc FLOAT(5),
    orientation VARCHAR(255),
    exterieur BOOLEAN,
    balcony BOOLEAN,
    garden BOOLEAN,
    parking int,
    ville VARCHAR(255),
    departement int ,
    date_fin_programme VARCHAR (255),
    adresse_entiere VARCHAR(255),
    date_extraction DATE, 
    PRIMARY KEY (id)
 );


 -- Create MCD tables

begin transaction;

CREATE TABLE typologie (
    id SERIAL,
    name VARCHAR (255),
	PRIMARY KEY (id)
);
CREATE TABLE orientation (
    id SERIAL,
    name VARCHAR (255),
	PRIMARY KEY (id)
);
CREATE TABLE departement (
    id SERIAL,
    name VARCHAR (255),
	PRIMARY KEY (id)
);

CREATE TABLE ville (
    id SERIAL,
    name VARCHAR (255),
    id_departement INT,
	PRIMARY KEY (id),
    FOREIGN KEY (id_departement) REFERENCES departement (id)
);

CREATE TABLE lotissement (
    id SERIAL,
    nb_piece int,
    prix_tva_reduit FLOAT(6),
    prix_tva_normal FLOAT(6),
    prix_ht FLOAT(6),
    prix_m_ht FLOAT(5),
    prix_m_ttc FLOAT(5),
    exterieur BOOLEAN,
    balcony BOOLEAN,
    parking int,
    adresse_entiere VARCHAR(255),
    id_ville INT,
    id_departement INT,
    id_orientation INT,
    id_typologie INT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_ville) REFERENCES ville (id),
    FOREIGN KEY (id_departement) REFERENCES departement (id),
    FOREIGN KEY (id_orientation) REFERENCES orientation (id),
    FOREIGN KEY (id_typologie) REFERENCES typologie (id)
);

-- Alter table Surface, etage, 

ALTER TABLE lotissement 
ADD surface FLOAT NULL,
ADD etage INT NULL,
ADD nom_du_programme VARCHAR(60) NULL,
ADD promoteur VARCHAR(30) NULL  


-- Select biens immo possédant un balcon

SELECT * FROM lotissement 
WHERE balcony == TRUE