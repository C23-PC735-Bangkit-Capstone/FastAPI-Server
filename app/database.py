from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configure the database connection
db_username = "your_username"
db_password = "your_password"
db_name = "your_database_name"
db_instance_connection_name = "your_instance_connection_name"

# Create the SQLAlchemy engine
engine = create_engine(
    f"mysql+mysqlconnector://{db_username}:{db_password}@localhost/{db_name}?unix_socket=/cloudsql/{db_instance_connection_name}"
)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
