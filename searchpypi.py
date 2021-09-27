#! python3
# searchpypi.py - Opens several search results


import requests, sys, webbrowser, bs4
headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.22", "Accept-Language": "en-US"}
print('Searching...') #display text while downloading the search results webpage
res = requests.get('http://pypi.org/search/?q=' + ''.join(sys.argv[1:]))
webbrowser.open('http://pypi.org/search/?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()
print(res.raise_for_status())


#Retrieve top search result links.

soup = bs4.BeautifulSoup(res.text, 'html.parser')


#TODO: Open a browser tab for each result.
link_elems = soup.select('.package-snippet') #looking at the elements, all the hyperlinks have class="package-snippet" in their code
#print(link_elems[1])
'''this will print out all of the various css for the search
results page. You can then check which element/attribute
you want to use for the rest of your code. In this case
the href is followed by the end of the URL for the search
results desired.'''
print(link_elems[1].get('href'))                     

num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i].get('href')
    print('Opening ' + url_to_open)
    webbrowser.open(url_to_open)

