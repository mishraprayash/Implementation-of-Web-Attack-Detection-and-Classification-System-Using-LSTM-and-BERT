# import logging
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from config import DATABASE_URL

# # Configure logging
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# logger = logging.getLogger(__name__)

# # Database setup
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# def init_db():
#     """Initialize the database connection and check if it's reachable."""
#     try:
#         with engine.connect() as conn:
#             logger.info("✅ Database connection successful.")
#     except Exception as e:
#         logger.error(f"❌ Database connection failed: {e}")
#         raise

import logging
from sqlalchemy import create_engine,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from config import DATABASE_URL

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Extract MySQL connection details
from urllib.parse import urlparse

db_url = urlparse(DATABASE_URL)
# extracting the database name
db_name = db_url.path[1:]  
base_db_url = f"{db_url.scheme}://{db_url.username}:{db_url.password}@{db_url.hostname}:{db_url.port}"

# Connect to MySQL without specifying a database
engine = create_engine(base_db_url, echo=False)

def create_database():
    """Ensure the database exists before proceeding."""
    try:
        with engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
            logger.info(f"✅ Database '{db_name}' ensured.")
    except OperationalError as e:
        logger.error(f"❌ Failed to create database: {e}")
        raise

create_database()

# Now connect to the actual database
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():

    """Initialize the database connection."""
    try:
        with engine.connect() as conn:
            logger.info("✅ Database connection successful.")
    except Exception as e:
        logger.error(f"❌ Database connection failed: {e}")
        raise
