# Projet tuteuré licence informatique UNC 2022 Lexika

Voici le github de notre projet tuteuré 'Lexika':  

-Avec les csv des données dans le dossier 'Csv'  
-Le code jinja et le html dans le dossier 'jinja',  
-et la base de donnée SQLite dans le dossier 'BDD'.  


Les scripts SQL permettant de reconstruire la base de données :  

CREATE TABLE entree(  
entree varchar(50) primary key not null,  
langue varchar(50) not null,  
categorie varchar(50));  

CREATE TABLE traduction(  
entree varchar(50) not null,  
traduction varchar(100) not null,  
sensTraduction varchar(100) not null,  
foreign key (entree) references entree(entree),  
primary key (entree, traduction));   

CREATE TABLE reference(  
entree varchar(50) not null,  
reference varchar(50),  
foreign key (entree) references entree(entree),  
foreign key (reference) references entree(entree),  
primary key (entree, reference));   


Les scripts SQL permettant d'insérer les données d'un csv dans la base de donnée:  
.mode csv  
.import entree.csv entree  
.import traduction.csv traduction  
.import reference.csv reference  

Les scripts SQL permettant d'exporter les données de la base en csv, utiliser dans le jinja:  
.mode csv  
.output select.csv  
select * from entree natural join reference natural join traduction;  
