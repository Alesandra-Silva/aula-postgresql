import psycopg2 as pg

from dotenv import load_dotenv
import os


#Carregar as variaveis do .env
load_dotenv()


params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "hort": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT"),
}
