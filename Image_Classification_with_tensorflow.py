from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
import tqdm

#APIキーの情報
key = "495466b46b3de2d36c1fc4da03a74af3"
secret = "ca2529800398220b"
wait_time = 1

#保存フォルダの指定
animal_name = sys.argv[1]
savedir = "./" + animal_name

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
	text = animal_name,
	per_page = 400,
	media = 'photos',
	sort = 'relevance',
	safe_search = 1,
	extras = 'url_q, licence'
)

photos = result['photos']
#pprint(photos)

for i, photo in enumerate(photos['photo']):
	url_q = photo['url_q']
	filepath = savedir + '/' + photo['id'] + '.jpg'
	if os.path.exists(filepath): continue
	urlretrieve(url_q, filepath)
	time.sleep(wait_time)
