
print("config.py")
from dotenv import load_dotenv
import os

load_dotenv(override=True)

class Config:

    print("congig de config.py")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mi_tienda.db' 