import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Function to scrape a single page and save data to a spreadsheet
def scrape_page(url, sheet):
    # Send a GET request to the page
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the information you need from the page
    # Here, we're just printing the page title as an example
    title = soup.find('title').get_text()
    print(f"Page Title: {title}")

    # Write the data to the spreadsheet
    sheet.append([url, title])

    # You can perform further processing or store the extracted data as per your requirement

# Main function to scrape all pages and save data to a spreadsheet
def scrape_website(base_url):
    # Create a new spreadsheet
    workbook = Workbook()
    sheet = workbook.active

    # Send a GET request to the base URL
    response = requests.get(base_url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the links on the page
    links = soup.find_all('a')

    # Scrape each page
    for link in links:
        # Construct the absolute URL
        url = base_url + link['href']

        # Call the scrape_page function
        scrape_page(url, sheet)

    # Save the spreadsheet
    workbook.save("scraped_data.xlsx")

# Specify the base URL of the website you want to scrape
base_url = 'https://mrpuffs.com/'
# Call the scrape_website function
scrape_website(base_url)
print(base_url)
