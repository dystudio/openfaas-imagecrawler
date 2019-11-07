from urllib.request import urlopen
import urllib.request
import json   
from bs4 import BeautifulSoup
import re

max_depth = 2 

def handle(req):

	url = req.strip()
	if not url.endswith("/"):
		url = url + "/"

	all_urls = []
	all_urls.append(url)
	find_all_urls(url, url, all_urls)
	all_urls = list(set(all_urls))
	all_images = find_all_images(all_urls)
	all_images = list(set(all_images))
	return json.dumps(all_images)


def find_all_images(all_urls):

	temp_images = []
	for url in all_urls:
		try:
			html = urlopen(url)
			bs = BeautifulSoup(html, 'html.parser')
			images = get_images(bs, url)
			temp_images.extend(images)
		except:
			# print("Error finding all images:"+url)
			nop = None

	return temp_images


def find_all_urls(root_url, url, all_urls,depth=1):

	if depth == max_depth:
		return

	temp_urls = []
	try:
		html = urlopen(url)
		bs = BeautifulSoup(html, 'html.parser')
		for a in bs.find_all('a', href=True):
			if a["href"].startswith(root_url) and a["href"] not in all_urls and a["href"] not in temp_urls:
				# print ("Found the URL:", a['href'])
				temp_urls.append(a["href"])
			elif not a["href"].startswith("mailto") and not a["href"].startswith("http") and not a["href"].startswith("..") and root_url+"/"+a["href"] not in all_urls and root_url+a["href"] not in temp_urls and root_url+"/"+a["href"] not in temp_urls:
				if a["href"].startswith("/"):
					# print ("Found the URL:", a["href"])
					temp_urls.append(root_url+a["href"][1:])
				else:
					# print ("Found the URL:", a["href"])
					temp_urls.append(root_url+a["href"])

	except:
		# print("Error loading URL:"+url)
		return 

	for c in temp_urls:
		all_urls.append(c)
		find_all_urls(root_url, c, all_urls, depth+1)


def get_images(bs, url):
	images_output = []
	images = bs.find_all('img', {'src': lambda s: s.endswith((".jpg", ".jpeg", ".png"))})
	for image in images: 

		if image["src"].startswith("http"):
			images_output.append(image["src"])
		elif image["src"].startswith("/"):
			images_output.append(url+image["src"][1:])
		else:
			images_output.append(url+image["src"])

	return images_output
