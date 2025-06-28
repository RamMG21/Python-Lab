import requests
from bs4 import BeautifulSoup

# URL of the web page you want to analyze
url = "https://www.mlb.com/brewers/stats/"

# Make an HTTP request to get the content of the page
response = requests.get(url)

# Verify that the request was successful
if response.status_code == 200:
    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements that contain the desired information
    # In this case, titles inside (<h2>, <p>, <h3> ...) tags
    titles = soup.find_all('td')

    # Ruta del archivo donde guardarás el texto
    file_path = "titles.txt"

    with open(file_path, "w", encoding="utf-8") as file:
        for i, title in enumerate(titles, start=1):
            file.write(f"{i}, {title.get_text()}\n")

    print(f"Los titulos se han guardardo en {file_path}")

    # Print the titles
    for i, title in enumerate(titles, start=1):
        print(f"{i}. {title.get_text()}")
else:
    print(f"Error accessing page: {response.status_code}")