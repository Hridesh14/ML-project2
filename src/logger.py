import sys
import os
import logging
from datetime import datetime
log_filename = f"log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
log_filepath = os.path.join("logs", log_filename)       
os.makedirs(os.path.dirname(log_filepath), exist_ok=True)
logging.basicConfig(
    filename=log_filepath,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
