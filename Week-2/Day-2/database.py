from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine

database_url="postgresql://postgres:password@localhost:5432/mydb"
engine=create_engine(database_url)

session_creation=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()
