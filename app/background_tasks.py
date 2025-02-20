# app/background_tasks.py

from db import SessionLocal
from model import RequestLog
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def save_log_entry(log_entry_data: dict):
    db = SessionLocal()
    try:
        log_entry = RequestLog(**log_entry_data)
        db.add(log_entry)
        db.commit()
        logger.info('Request Logged Success')
    except Exception as e:
        db.rollback()
        # Optionally log the exception (e.g., using logging module)
        logger.info('Could not Log the Request to the Database')
        logger.info(e)
        
    finally:
        db.close()
        logger.info('DB Closed')
