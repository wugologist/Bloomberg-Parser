from BeautifulSoup import BeautifulSoup
import urllib2

article = open('article.txt', 'w')

links = []
linkstrings = []
html_page = urllib2.urlopen("http://www.bloomberg.com/archive/news")
soup = BeautifulSoup(html_page)

data = soup.findAll('ul', attrs={'class':'stories'});

for div in data:
    links = div.findAll('a')
    for a in links:
        #print "http://www.bloomberg.com/" + a['href'];
		linkstrings.append("http://www.bloomberg.com/" + a['href'])
		
samplelinks = linkstrings[0:1]

for link in samplelinks:
	print link
	
	page = urllib2.urlopen(str(link))
	pagesoup = BeautifulSoup(page)
	
	paragraphs = pagesoup.findAll('div', attrs={'class' : 'article_body'})
	
	for p in paragraphs:
		print str(p)
		article.write(str(p))