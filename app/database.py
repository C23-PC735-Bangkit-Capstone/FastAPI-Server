import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from google.cloud.sql.connector import Connector, IPTypes

INSTANCE_CONNECTION_NAME = "bangkit-capstone-387911:asia-southeast2:cloud-sql-fastapi"
DB_USER = "postgres"
DB_PASS = "cloud-sql-fastapi-password-12345!"
DB_NAME = "smart-vibration-monitoring"
PRIVATE_IP = False

# Set the environment variables
os.environ["PRIVATE_IP"] = str(PRIVATE_IP)
os.environ["INSTANCE_CONNECTION_NAME"] = INSTANCE_CONNECTION_NAME
os.environ["DB_USER"] = DB_USER
os.environ["DB_PASS"] = DB_PASS
os.environ["DB_NAME"] = DB_NAME

# Cloud SQL Python Connector creator function
def getconn():
    # if env var PRIVATE_IP is set to True, use private IP Cloud SQL connections
    ip_type = IPTypes.PRIVATE if os.getenv("PRIVATE_IP") == "True" else IPTypes.PUBLIC
    # if env var DB_IAM_USER is set, use IAM database authentication
    user, enable_iam_auth = (
        (os.getenv("DB_IAM_USER"), True)
        if os.getenv("DB_IAM_USER")
        else (os.getenv("DB_USER"), False)
    )
    # initialize Cloud SQL Python connector object
    with Connector(ip_type=ip_type, enable_iam_auth=enable_iam_auth) as connector:
        conn = connector.connect(
            os.getenv("INSTANCE_CONNECTION_NAME"),
            "pg8000",
            user=user,
            password=os.getenv("DB_PASS", ""),
            db=os.getenv("DB_NAME"),
        )
        return conn

SQLALCHEMY_DATABASE_URL = "postgresql+pg8000://"

engine = create_engine(SQLALCHEMY_DATABASE_URL, creator=getconn)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Reflect existing tables (optional)
metadata = MetaData()
metadata.reflect(bind=engine)

# Bind metadata objects of your models
metadata.bind = engine
metadata.reflect(bind=engine, only=[
    "vibration_health",
    "vibration",
    "users",
    "pond",
    "device",
])

# Create the tables
metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
