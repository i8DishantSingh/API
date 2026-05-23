from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os 

load_dotenv()
    

engine=create_engine(
    f"{os.getenv("DATA_BASE_URL")}",
    echo=True
)

Base=declarative_base()
Session = sessionmaker()

