# ScrapeMate

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

ScrapeMate is a lightweight Python package designed for quick and easy web scraping. It provides a simple interface for fetching and parsing web pages to extract useful information.

## Features
- **Fetch HTML content** from a given URL.
- **Parse HTML** to extract elements based on tags and class names.
- **Save extracted data** to various formats (CSV and JSON).
- **Easy-to-use command-line interface** (planned for future updates).

## Installation
ScrapeMate uses Poetry for dependency management and project building. To install the package and its dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd ScrapeMate
   ```

2. **Install dependencies**:
   ```bash
   poetry install
   ```

## Usage
Here's how to use ScrapeMate in your Python projects:

### Fetch and Parse Content:
```python
from scrape_mate.scraper import fetch_content, parse_html

# Fetch content from a web page
url = "https://example.com"
content = fetch_content(url)

# Parse the content to find all div elements with a specific class
elements = parse_html(content, 'div', 'example-class')
for element in elements:
    print(element.text)
```

## Building and Packaging
To build the project into a distributable format (e.g., a wheel), use:
```bash
poetry build
```
This will create the package files in the `dist/` directory.

## Running Tests
ScrapeMate includes unit tests to verify its functionality. To run the tests, use:
```bash
poetry run pytest tests/
```

## Project Versioning
Versioning is handled by Poetry and specified in the `pyproject.toml` file.

## Replicable Build
To replicate the project build and install the package, run:
```bash
poetry install
```
This command installs all dependencies and sets up the environment to build, test, and run the project.

## Contributing
Contributions are welcome! Feel free to fork the project, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
