# Web Scraping Script

This repository contains a Python script for web scraping product information from an e-commerce website using the `requests` library and `BeautifulSoup`.

## Prerequisites

- Python 3.10
- Install required libraries by running: `pip install requests beautifulsoup4`

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git


2. Navigate to the project directory:
    ```bash
    cd your-repo

3. Run the script:
   ```bash
   python scrape.py
  Follow the prompts to enter the URL of the product page you want to scrape.

## Script Details
The script (`scrape. py`) performs the following tasks:
  • Accepts a URL as input from the user.
  • Fetches the HTML content of the provided URL using the `requests` library.
  • Parses the HTML content with `BeautifulSoup`.
  • Extracts and displays the product name, ratings, and price.
Note: Please use this script responsibly and adhere to the terms of use of the website you
are scraping. Be aware that websites may have restrictions on scraping activities.

## Example Output
    ```bash
      Enter the url: https://flipkart.com/product-page
      Name of the product: Example Product
      Ratings: 4.5*
      Price: $19.99
## Contributing
  Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
