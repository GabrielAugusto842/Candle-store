import os #operational system environment variable
from dotenv import load_dotenv

load_dotenv() #Carrega as variáveis do .env

class Config:
    #security, environment variable secret_key
    SECRET_KEY = os.getenv('SECRET_KEY')
    #Sets database connection URL using variable in .env
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    #Disable SQLAlchemy modification tracking and improves performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #Validate tokens JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')