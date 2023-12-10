#!/bin/bash
DB_HOST="localhost"
DB_USER="postgres"
DB_PASSWORD="postgres"
DB_NAME="uecebet"

EMAIL1="user1@gmail.com"
NOME1="user1"
TIPO_USUARIO1=0
CPF1="00000000001"
NACIONALIDADE1="brasileiro"
NASCIMENTO1="2023-12-01"
SALDO1=20
SENHA1="pbkdf2:sha256:600000\$KFdTnb1DSbhi2ULO\$8059293e1ade87aa667f6f9f90ad360efad0ecd50805912cf2f1b9ee3522b4d2"

EMAIL2="adm@gmail.com"
NOME2="admin"
TIPO_USUARIO2=1
CPF2="00000000000"
NACIONALIDADE2="brasileiro"
NASCIMENTO2="2003-06-23"
SALDO2=20
SENHA2="pbkdf2:sha256:600000\$CkLNDfHU2YJ6WimA\$b3f21e2e7de092d3767d6744afd09ce0585c89fccb1a0fe5b3dd0ac57c691638"

EMAIL3="user2@gmail.com"
NOME3="user2"
TIPO_USUARIO3=0
CPF3="00000000002"
NACIONALIDADE3="brasileiro"
NASCIMENTO3="2023-12-01"
SALDO3=20
SENHA3="pbkdf2:sha256:600000\$KFdTnb1DSbhi2ULO\$8059293e1ade87aa667f6f9f90ad360efad0ecd50805912cf2f1b9ee3522b4d2"

EMAIL4="user3@gmail.com"
NOME4="user3"
TIPO_USUARIO4=0
CPF4="00000000003"
NACIONALIDADE4="brasileiro"
NASCIMENTO4="2023-12-01"
SALDO4=20
SENHA4="pbkdf2:sha256:600000\$KFdTnb1DSbhi2ULO\$8059293e1ade87aa667f6f9f90ad360efad0ecd50805912cf2f1b9ee3522b4d2"
 
INSERT_QUERY1="INSERT INTO usuarios (email, nome, tipo_usuario, cpf, nacionalidade, nascimento, saldo, senha) VALUES
               ('$EMAIL1', '$NOME1', $TIPO_USUARIO1, '$CPF1', '$NACIONALIDADE1', '$NASCIMENTO1', $SALDO1, '$SENHA1');"
INSERT_QUERY2="INSERT INTO usuarios (email, nome, tipo_usuario, cpf, nacionalidade, nascimento, saldo, senha) VALUES
               ('$EMAIL2', '$NOME2', $TIPO_USUARIO2, '$CPF2', '$NACIONALIDADE2', '$NASCIMENTO2', $SALDO2, '$SENHA2');"
INSERT_QUERY3="INSERT INTO usuarios (email, nome, tipo_usuario, cpf, nacionalidade, nascimento, saldo, senha) VALUES
               ('$EMAIL3', '$NOME3', $TIPO_USUARIO3, '$CPF3', '$NACIONALIDADE3', '$NASCIMENTO3', $SALDO3, '$SENHA3');"             
INSERT_QUERY4="INSERT INTO usuarios (email, nome, tipo_usuario, cpf, nacionalidade, nascimento, saldo, senha) VALUES
               ('$EMAIL4', '$NOME4', $TIPO_USUARIO4, '$CPF4', '$NACIONALIDADE4', '$NASCIMENTO4', $SALDO4, '$SENHA4');"


               
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -U $DB_USER -d $DB_NAME -c "$INSERT_QUERY1"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -U $DB_USER -d $DB_NAME -c "$INSERT_QUERY2"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -U $DB_USER -d $DB_NAME -c "$INSERT_QUERY3"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -U $DB_USER -d $DB_NAME -c "$INSERT_QUERY4"