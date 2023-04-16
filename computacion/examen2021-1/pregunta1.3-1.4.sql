
--creando las tablas

create table diciplinas (id int primary key, nombre varchar(),reglas text)


create table jjoos (id int primary key, nombre varchar(),edicion varchar())

create table competencias (num_serie int primary key, diciplina_id int foreign key references diciplinas(id),categoria varchar(),timestamp timestamp, estado varchar(),tipo varchar())
create table medallas (id int primary key, tipo varchar())

create table paises (id int primary key, nombre varchar(),poblacion int)
create table deportistas (rut varchar() primary key , id_pais int foreign key references paises(id),nombre varchar(),edad int,sexo varchar())
create table records(id int primary key , competencia_id foreign key references competencias(id), valor float,  tipo varchar)


create table ganan (medalla_id int foreign key references medallas(id), deportista_id int foreign key references deportistas(id))
create table reparten((medalla_id int foreign key references medallas(id),comp_numserie int foreign key references competencias(id))

create table villas_olimnpicas(id int primary key , id_pais foreign key references paises(id), direccion varchar(), capacidad int , ciudad varchar())
create table descanzan (rut_deportista varchar foreign key references deportistas(rut),id_villa int foreign key references villas_olimnpicas(id), fecha date)

create table planifica (id_competencia int foreign key references competencias(id) , id_jo int foreign key references jjoos(id))

create table dispone (id_pais int foreign key references pais(id),id_villa int foreign key references villas_olimnpicas(id))

create table obtiene(id_record int foreign key references records(id), id_deportista int foreign key references deportistas(rut))

create table organizan (id_jo int foreign key references jjoos(id), id_pais int foreign key references paises(id) , ciudad varchar, año int)

create table resultados(deportista_id int foreign key references deportistas(rut),id_villa int foreign key references villas_olimnpicas(id), resultado varchar)

--consultas no alcance x tiempo :(

--Nombres y nacionalidades de deportistas que compiten en más de una disciplina, junto con el nombre de esas disciplinas.

-- Nombres de países cuyas atletas mujeres obtuvieron más medallas (totales) que los atletas hombres.

-- Ranking de países en el medallero.

--- Cantidad de países que no tienen un récord olímpico