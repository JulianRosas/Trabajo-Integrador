
CREATE DATABASE El_Lector;
use  El_Lector;    

create table Pais(
id int primary key, 
nombre varchar(15), 
descripcion varchar(50));

create table Tipo_documento(
id int primary key,
nombre varchar(15), 
descripcion varchar(50));

create table Domicilio(
id int primary key, 
calle varchar(15), 
altura int,  
localidad varchar(50), 
piso int);

create table Genero(
id int primary key, 
nombre varchar(15), 
descripcion varchar(50));

create table Imprenta(
id int primary key, 
nombre varchar(15), 
telefono int, 
sitio_web varchar(20), 
email varchar(20),
id_domicilio int,
constraint foreign key (id_domicilio) references Domicilio(id));
drop table Imprenta;
drop table Libro;
drop table Genero_libro;
drop table Editor;

create table Persona(
id int primary key, 
nombre varchar(15), 
apellido varchar(15), 
telefono int, 
id_domicilio int, 
constraint foreign key (id_domicilio) references Domicilio(id), 
id_tipo_documento int, 
constraint foreign key (id_tipo_documento) references Tipo_documento(id));

create table Autor( 
nro_documento int primary key, 
apellido varchar(15), 
id_persona int, 
constraint foreign key (id_persona) references Persona(id), 
id_pais int, 
constraint foreign key (id_pais) references Pais(id));

create table Libro(
isbn int primary key, 
titulo varchar(20), 
cant_paginas int, 
reseña varchar(100), 
id_imprenta int, 
constraint foreign key (id_imprenta) references Imprenta(id),
nro_documento_autor int,
constraint foreign key (nro_documento_autor) references Autor(nro_documento));

create table Genero_libro(
id int primary key, 
isbn_libro int, 
constraint foreign key (isbn_libro) references Libro(isbn), 
id_genero int, 
constraint foreign key (id_genero) references Genero(id));

create table Editor(
cuil int primary key, 
id_persona int, 
constraint foreign key (id_persona) references Persona(id), 
isbn_libro int, 
constraint foreign key (isbn_libro) references Libro(isbn));