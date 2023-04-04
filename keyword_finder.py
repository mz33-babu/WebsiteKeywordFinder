import requests
from bs4 import BeautifulSoup
import webbrowser

# List of preselected websites
websites = [
    ('Example Site 1', 'https://www.example1.com'),
    ('Example Site 2', 'https://www.example2.com'),
    ('Example Site 3', 'https://www.example3.com')
]

# List of search terms
search_terms = ['keyword1', 'keyword2', 'keyword3']

# Function to search for keywords in a website's content
def search_keywords(url, keywords):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text().lower()

    for keyword in keywords:
        if keyword.lower() in text:
            return True
    return False

# Main function
def main():
    for name, url in websites:
        try:
            if search_keywords(url, search_terms):
                print(f'Keyword(s) found in {name} ({url})')
                webbrowser.open(url, new=2)
            else:
                print(f'No keywords found in {name} ({url})')
        except requests.exceptions.RequestException as e:
            print(f'Error while processing {name} ({url}): {e}')

if __name__ == '__main__':
    main()
