#! python3
#downloadxkcd.py - Downloads every single XKCD comic.

import requests, os, bs4, pprint

url = 'https://xkcd.com'    #starting url
os.makedirs('xkcd', exist_ok = True)    #store comics in ./xkcd

while not url.endswith('2400'):
    #TODO: Download the page
    print('Downloading the page %s... ' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    

    #TODO: Find the URL of the comic image.    
    comic_elem = soup.select('#comic img')
        #^ when using .select(), you use CSS format. In this case, the #
        # symbol refers to an ID type.
        # the img comes from the next attribute going down the html under the comic ID

    comic_num = int(soup.select('a[rel="prev"]')[0].get('href').strip('/')) + 1
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        comic_url = 'https:' + comic_elem[0].get('src')
        print(comic_url)
    #TODO: Downlaod the image.
        print('Downloading the image %s...' % ((comic_url)))
        res = requests.get(comic_url)
        res.raise_for_status()

    #TODO: Save the image to ./xkcd
        image_file = open(os.path.join('xkcd', str(comic_num) + ' - ' + os.path.basename(comic_url)), 'wb')

        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    #TODO: Get the Prev. Buttons URL.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')
print('Done')
