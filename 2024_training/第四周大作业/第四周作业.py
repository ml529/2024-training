import json
import os
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Create database connection
engine = create_engine('mysql://your_username:your_password@localhost/your_database')
Base = declarative_base()
# Define data table model
class DataInfo(Base):
    __tablename__ = 'DataInfo'
    id = Column(Integer, primary_key=True)
    file_path = Column(String(255))
    text_content = Column(Text)
    file_size = Column(Integer)
# Create data table
Base.metadata.create_all(engine)
# Read data_info.json file
with open('data_info.json', 'r') as file:
    data_info = json.load(file)
# Create session
Session = sessionmaker(bind=engine)
session = Session()
# Read file paths from data_info.json and store relevant information in database table
for entry in data_info:
    file_path = os.path.abspath(entry.get("resource"))
    if file_path:
        if file_path.endswith(".txt"):
            with open(file_path, 'r') as text_file:
                text_content = text_file.read()
            new_data = DataInfo(file_path=file_path, text_content=text_content)
        elif file_path.endswith(".bin"):
            file_size = os.path.getsize(file_path)
            new_data = DataInfo(file_path=file_path, file_size=file_size)
        session.add(new_data)
# Commit changes and close session
session.commit()
session.close()

