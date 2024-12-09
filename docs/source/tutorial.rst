Tutorial
========

Welcome to the ScrapeMate tutorial! This guide will walk you through the basics of using ScrapeMate to scrape and parse web content effectively.

.. contents::
   :local:
   :depth: 2

Introduction
------------

ScrapeMate is a lightweight Python package designed for quick and easy web scraping. Whether you're collecting data for research, monitoring websites, or automating tasks, ScrapeMate provides a simple interface to get the job done.

In this tutorial, you'll learn how to:

1. **Install ScrapeMate**
2. **Fetch HTML Content from a URL**
3. **Parse HTML to Extract Specific Elements**
4. **Save Extracted Data to CSV and JSON Formats**
5. **Handle Common Use Cases**

.. note::

   Before you begin, ensure that you have Python 3.8+ and Poetry installed on your system. If not, follow the [Prerequisites](#prerequisites) section to set them up.

Prerequisites
-------------

Before you begin, ensure you have the following:

- **Python 3.8+** installed on your system.
- **Poetry** installed for dependency management. If you don't have Poetry installed, you can install it by following the [Poetry Installation Guide](https://python-poetry.org/docs/#installation).

Installation
------------

To start using ScrapeMate, you'll first need to install it along with its dependencies.

1. **Clone the Repository**

   Begin by cloning the ScrapeMate repository to your local machine:

   .. code-block:: bash

       git clone https://github.com/your-username/ScrapeMate.git
       cd ScrapeMate

2. **Install Dependencies with Poetry**

   Install the necessary dependencies using Poetry:

   .. code-block:: bash

       poetry install

   This command sets up a virtual environment and installs all required packages specified in the `pyproject.toml` file.

3. **Activate the Virtual Environment**

   Activate the Poetry-managed virtual environment:

   .. code-block:: bash

       poetry shell

Fetching and Parsing Content
----------------------------

With ScrapeMate installed, you're ready to fetch and parse web content.

1. **Fetch HTML Content from a URL**

   Use the `fetch_content` function to retrieve HTML content from a specified URL.

   .. code-block:: python

       from scrape_mate.scraper import fetch_content

       # Specify the URL you want to scrape
       url = "https://example.com"

       # Fetch the HTML content
       html_content = fetch_content(url)

       print(html_content)  # Prints the raw HTML content

   **Explanation:**

   - **`fetch_content(url)`**: Sends an HTTP GET request to the provided URL and returns the HTML content as a string.

2. **Parse HTML to Extract Specific Elements**

   Use the `parse_html` function to parse the fetched HTML and extract elements based on tag names and optional class names.

   .. code-block:: python

       from scrape_mate.scraper import parse_html

       # Define the HTML tag you want to search for, e.g., 'div'
       element_tag = "div"

       # (Optional) Define the class name to filter elements
       class_name = "example-class"

       # Parse the HTML content to find matching elements
       elements = parse_html(html_content, element_tag, class_name)

       # Iterate through the extracted elements and print their text content
       for element in elements:
           print(element.text)

   **Explanation:**

   - **`parse_html(html_content, element_tag, class_name)`**: Parses the HTML content to find all elements matching the specified tag and class name. Returns a list of BeautifulSoup Tag objects.

Saving Extracted Data
---------------------

After extracting the desired elements, you can save the data in various formats like CSV and JSON.

1. **Save Data to CSV**

   Use the `save_to_csv` function to save the extracted data to a CSV file.

   .. code-block:: python

       from scrape_mate.file_saver import save_to_csv

       # Prepare data as a list of rows (each row is a list of values)
       data = [
           ["Title", "Description"],
           ["Example Title 1", "Description for title 1"],
           ["Example Title 2", "Description for title 2"],
           # Add more rows as needed
       ]

       # Specify the filename for the CSV
       csv_filename = "extracted_data.csv"

       # Save the data to CSV
       save_to_csv(data, csv_filename)

       print(f"Data successfully saved to {csv_filename}")

   **Explanation:**

   - **`save_to_csv(data, filename)`**: Writes the provided data to a CSV file with the specified filename.

2. **Save Data to JSON**

   Use the `save_to_json` function to save the extracted data to a JSON file.

   .. code-block:: python

       from scrape_mate.file_saver import save_to_json

       # Prepare data as a dictionary or any JSON-serializable object
       data = {
           "titles": ["Example Title 1", "Example Title 2"],
           "descriptions": ["Description for title 1", "Description for title 2"],
           # Add more key-value pairs as needed
       }

       # Specify the filename for the JSON
       json_filename = "extracted_data.json"

       # Save the data to JSON
       save_to_json(data, json_filename)

       print(f"Data successfully saved to {json_filename}")

   **Explanation:**

   - **`save_to_json(data, filename)`**: Serializes the provided data to a JSON file with the specified filename.

Handling Common Use Cases
------------------------

ScrapeMate is versatile and can handle various web scraping scenarios. Below are a couple of common use cases to get you started.

1. **Scraping Multiple Pages**

   Suppose you want to scrape data from multiple pages of a website. You can loop through a list of URLs and aggregate the data.

   .. code-block:: python

       from scrape_mate.scraper import fetch_content, parse_html
       from scrape_mate.file_saver import save_to_json

       # List of URLs to scrape
       urls = [
           "https://example.com/page1",
           "https://example.com/page2",
           "https://example.com/page3",
       ]

       # Initialize a list to hold all extracted data
       all_data = []

       for url in urls:
           html = fetch_content(url)
           elements = parse_html(html, "div", "example-class")

           for element in elements:
               title = element.find("h2").text.strip()
               description = element.find("p").text.strip()
               all_data.append({"title": title, "description": description})

       # Save the aggregated data to JSON
       save_to_json(all_data, "all_extracted_data.json")

       print("All data successfully saved to all_extracted_data.json")

2. **Automating the Scraping Process**

   You can automate the scraping process by scheduling your script to run at regular intervals using tools like **cron** (on Unix-based systems) or **Task Scheduler** (on Windows).

   **Example Cron Job (Runs Daily at Midnight):**

   1. **Open the cron table:**

      .. code-block:: bash

          crontab -e

   2. **Add the following line to schedule the scraping script:**

      .. code-block:: bash

          0 0 * * * /path/to/your/virtualenv/bin/python /path/to/your/project/ScrapeMate/scrape_script.py

      **Explanation:**

      - **`0 0 * * *`**: Specifies the job to run daily at midnight.
      - **`/path/to/your/virtualenv/bin/python`**: Path to the Python interpreter in your virtual environment.
      - **`/path/to/your/project/ScrapeMate/scrape_script.py`**: Path to your scraping script.

   **Note:** Ensure your script handles potential errors and logs its activities for easier troubleshooting.

Conclusion
----------

Congratulations! You've successfully completed the ScrapeMate tutorial. You've learned how to install ScrapeMate, fetch and parse web content, save extracted data, and handle common scraping scenarios. With these skills, you're well-equipped to leverage ScrapeMate for your web scraping projects.

What's Next?
------------

- **Explore Advanced Features:** Dive deeper into ScrapeMate's capabilities, such as handling authentication, managing sessions, or integrating with databases.
- **Contribute to ScrapeMate:** If you have ideas for improvements or new features, consider contributing to the project.
- **Share Your Projects:** Showcase what you've built using ScrapeMate, whether it's data analysis, reporting, or automation tools.

Additional Resources
--------------------

- **ScrapeMate Documentation:** `Link to your reference documentation <https://github.com/your-username/ScrapeMate/docs/build/html/index.html>`_
- **Sphinx Documentation:** https://www.sphinx-doc.org/en/master/
- **BeautifulSoup Documentation:** https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- **Requests Documentation:** https://requests.readthedocs.io/en/latest/
- **Poetry Documentation:** https://python-poetry.org/docs/

.. note::

   For further assistance or questions, feel free to reach out through the project's repository.