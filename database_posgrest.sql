create database bd_prediccion

create table usuario(
id_us serial,
nombre varchar(30),
clave varchar(10)
);
select * from usuario
insert into usuario(nombre,clave) values ('Josue','1234')
insert into usuario(nombre,clave) values ('Admin','Admin')