import csv
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='file_saver.log',
    filemode='w'
)

def save_to_csv(data, filename):
    """Saves data to a CSV file."""
    logging.info(f"Saving data to CSV file: {filename}")
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                writer.writerow(row)
            logging.info(f"Data successfully saved to {filename}")
    except Exception as e:
        logging.error(f"Failed to save data to CSV file {filename}: {e}")
        raise

def save_to_json(data, filename):
    """Saves data to a JSON file."""
    logging.info(f"Saving data to JSON file: {filename}")
    try:
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
            logging.info(f"Data successfully saved to {filename}")
    except Exception as e:
        logging.error(f"Failed to save data to JSON file {filename}: {e}")
        raise
