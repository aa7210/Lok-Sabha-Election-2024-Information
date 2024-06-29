import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page to scrape
url = "https://results.eci.gov.in/AcResultByeJune2024/"

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the divs with the class "box-content"
divs = soup.find_all('div', class_='box-content')

# Prepare a list to store the extracted data
data = []

# Iterate through each div and extract the required information
for div in divs:
    constituency_name = div.find('h3').text if div.find('h3') else ''
    state = div.find('h4').text if div.find('h4') else ''
    ruling_person = div.find('h5').text if div.find('h5') else ''
    party = div.find('h6').text if div.find('h6') else ''
    data.append([constituency_name, state, ruling_person, party])

# Create a DataFrame from the extracted data
df = pd.DataFrame(data, columns=['Constituency Name', 'State', 'Ruling Person', 'Party'])

# Save the DataFrame to a CSV file
df.to_csv('election_results.csv', index=False)

print("Data has been scraped and saved to election_results.csv")
