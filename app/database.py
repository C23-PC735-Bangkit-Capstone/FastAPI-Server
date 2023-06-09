from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configure the database connection
db_username = "postgres"
db_password = "janganlupa75"
db_name = "smartmonitoringapp"
db_instance_connection_name = None

if db_instance_connection_name:
    # Create the SQLAlchemy engine for Google Cloud SQL
    engine = create_engine(
        f"mysql+mysqlconnector://{db_username}:{db_password}@localhost/{db_name}?unix_socket=/cloudsql/{db_instance_connection_name}"
    )
else:
    # Create the SQLAlchemy engine for localhost
    engine = create_engine(
        f"mysql+mysqlconnector://{db_username}:{db_password}@localhost/{db_name}"
    )

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
