from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen


url = 'http://quotes.yourdictionary.com/theme/marriage/'
response = urlopen(url).read()
soup = BeautifulSoup(response)

quotes = soup.findAll('p', attrs={'class': 'quoteContent'})
five_quotes = quotes[0:5]
for quote in five_quotes:
    print quote.string
