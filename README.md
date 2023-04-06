# Keyword Finder

This Python script searches for specified keywords on a list of preselected web pages. When a keyword is found, the script updates the user with the name of the website and opens the web page in the default browser.

# Requirements
* `Python 3.x`
* `requests`
* `beautifulsoup4`

# Installation
1. Download the `keyword_finder.py` script.
```bash
git clone https://github.com/mz33-babu/WebsiteKeywordFinder.git
```

2. Install the required libraries using the following command:
```bash
pip install -r requirements.txt
```

# Usage
1. Edit the `keyword_finder.py` script to include the list of preselected websites and search terms:
```css
websites = [
    ('Example Site 1', 'https://www.example1.com'),
    ('Example Site 2', 'https://www.example2.com'),
    ('Example Site 3', 'https://www.example3.com')
]

search_terms = ['keyword1', 'keyword2', 'keyword3']
```
Replace the example websites and search terms with the ones you want to use.

2. Run the script
```css
python keyword_finder.py
```
The script will search for the specified keywords in the provided websites, print the results, and open the matching web pages in your default browser.

# License
This project is released under the [MIT License](https://opensource.org/license/mit/).

