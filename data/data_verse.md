
What is Webscraping
How to webcrap with html, xml, json (public api, it is typically like python dictionary)

Web scraping tools: Scrapy, BeautifulSoup4, Selenium, Requests.

Web scraping vs API's


Tools for webscraping with python
- BeautifulSoup bs4
- Selenium
- Flask
- Scrapy


Different Types of Websites
- Static & Dynamic Website


HTML
- HTML is the language of the internet and to scrap data from the internet, you need to understand
html. class, id, tags, etc.

https://developer.mozilla.org/en-US/docs/Web/HTML




Webscraping
- Get URL
- Asssign headers, what is the importance of headers
- Check Statuscode 
- Different Types of Statuscode
- Pass url content as content
- Parse into BeautifulSoup 
- Various syntax in BeautifulSoup
    - title
    - title_name
    - title.string
    - find
    - find_all
    - get_text

- Inspect website to collect your data
    - type of house
    - price of house
    - location

- change price from string to int type
    - df['Price'] = df['Price'].astype(str).str.replace(',', '')
- unique values of location
- extract location with split to get location
- type of house (duplex, terrace, etc)
- average price of homes 
    - use groupby to check average price of homes by location
    - most popular house type
    - average price of houses by their types

price regex pattern: re.search(r'[\d,]+')
currency regex pattern: re.search(r'[\$|N]')


Assignment 

- Scrap 1000 rows of data from Nigeria property https://nigeriapropertycentre.com/
- Cleaned
- Answer the following questions
     - average price of homes by location
     - average price of homes by states
     - popular house type
     - average price of house type