"""
file_saver.py

This module provides functionalities to save data in various file formats.
It includes methods to save data to CSV and JSON files, handling potential
file I/O errors and logging the processes.

Dependencies:
- csv
- json
- logging
"""

import csv
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="file_saver.log",
    filemode="w",
)


def save_to_csv(data, filename):
    """
    Saves a list of data to a CSV file.

    Writes the provided data to a CSV file specified by the filename.
    Each item in the data list is written as a separate row in the CSV file.
    Logs the process and handles potential file I/O errors.

    Args:
        data (list[list[Any]]): A list of rows, where each row is a list of values to be written to the CSV.
        filename (str): The name (including path) of the CSV file to save the data to.

    Raises:
        IOError: If an I/O error occurs during file writing.
        Exception: For other unexpected errors during the saving process.
    """
    logging.info(f"Saving data to CSV file: {filename}")
    try:
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                writer.writerow(row)
            logging.info(f"Data successfully saved to {filename}")
    except IOError as e:
        logging.error(f"I/O error occurred while saving to CSV file {filename}: {e}")
        raise
    except Exception as e:
        logging.error(f"Failed to save data to CSV file {filename}: {e}")
        raise


def save_to_json(data, filename):
    """
    Saves data to a JSON file.

    Serializes the provided data to a JSON-formatted file specified by the filename.
    Logs the process and handles potential file I/O and serialization errors.

    Args:
        data (Any): The data to be serialized and saved to the JSON file. This can be any serializable Python object.
        filename (str): The name (including path) of the JSON file to save the data to.

    Raises:
        TypeError: If the data provided is not JSON serializable.
        IOError: If an I/O error occurs during file writing.
        Exception: For other unexpected errors during the saving process.
    """
    logging.info(f"Saving data to JSON file: {filename}")
    try:
        with open(filename, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
            logging.info(f"Data successfully saved to {filename}")
    except TypeError as e:
        logging.error(
            f"Data provided is not JSON serializable for file {filename}: {e}"
        )
        raise
    except IOError as e:
        logging.error(f"I/O error occurred while saving to JSON file {filename}: {e}")
        raise
    except Exception as e:
        logging.error(f"Failed to save data to JSON file {filename}: {e}")
        raise
