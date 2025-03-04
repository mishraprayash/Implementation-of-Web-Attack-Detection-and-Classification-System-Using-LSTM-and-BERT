
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
    except Exception as e:
        db.rollback()
        logger.info('Could not Log the Request to the Database')
        logger.info(e)
        
    finally:
        db.close()
