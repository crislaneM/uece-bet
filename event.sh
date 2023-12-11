#!/bin/bash
DB_HOST="localhost"
DB_USER="postgres"
DB_PASSWORD="postgres"
DB_NAME="uecebet"

ID_1=2
TIME_1_1="Flamengo"
TIME_2_1="Vasco"
ODD_TIME_1_1=4.2
ODD_TIME_2_1=1.4
ODD_EMPATE_1=2.45
DATA="2023-12-01"
DESCRICAO='Evento 3'
ID_ADM_1=2
EVENTO_STATUS=True

ID_2=3
TIME_1_2="Botafogo"
TIME_2_2="Pipoqueiros FC"
ODD_TIME_1_2=10.4
ODD_TIME_2_2=1.7
ODD_EMPATE_2=1.2
DATA_2="2023-12-01"
DESCRICAO_2='Evento 2'
ID_ADM_2=2
EVENTO_STATUS_2=True

INSERT_QUERY1="INSERT INTO eventos (id, time_1, time_2, odd_time1, odd_time2, odd_empate, data, descricao, id_adm, evento_status) VALUES
               ('$ID_1', '$TIME_1_2', '$TIME_2_2', $ODD_TIME_1_2, $ODD_TIME_2_2, $ODD_EMPATE_2, '$DATA_2', '$DESCRICAO_2', $ID_ADM_2, $EVENTO_STATUS_2);"

INSERT_QUERY2="INSERT INTO eventos (id, time_1, time_2, odd_time1, odd_time2, odd_empate, data, descricao, id_adm, evento_status) VALUES
               ('$ID_2','$TIME_1_1', '$TIME_2_1', $ODD_TIME_1_1, $ODD_TIME_2_1, $ODD_EMPATE_1, '$DATA', '$DESCRICAO', $ID_ADM_1, $EVENTO_STATUS);"

PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -U $DB_USER -d $DB_NAME -c "$INSERT_QUERY1"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -U $DB_USER -d $DB_NAME -c "$INSERT_QUERY2"