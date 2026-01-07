from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger = get_logger(__name__)

def divide_numbers(a, b):
    """Function to divide two numbers and log the operation."""
    try:
        result = a / b
        logger.info("divide 2 nums")
        return result
    except Exception as e:
        logger.error("Error occurred during division")
        raise CustomException("Custom error zero division", sys)
    
if __name__ == "__main__":
    try:
        logger.info("Starting division operation.")
        divide_numbers(10, 0)
    except CustomException as ce:
        logger.error(str(ce))