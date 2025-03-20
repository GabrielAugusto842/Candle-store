from app import db #used to manipulate the database

#initialize the databases
def init_db():
    #Create all tables
    db.create_all