
CREATE DATABASE my_database;

USE my_database;

CREATE TABLE users (
    full_name VARCHAR(255),
    date_of_birth DATE,
    cpf INT,
    email VARCHAR(255),
    phone INT
);

CREATE TABLE address (
    road VARCHAR(255),
    neighborhood VARCHAR(255),
    city VARCHAR(255),
    uf VARCHAR(2),
    postcode INT
);