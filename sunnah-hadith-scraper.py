from bs4 import BeautifulSoup
import urllib
import os
import sys
import requests

dir = os.path.dirname(os.path.abspath(__file__))
hadithFolder = dir +"\\Hadith"

if not os.path.exists(hadithFolder):
        os.makedirs(hadithFolder)

print "Enter the url: "
main_url = raw_input();
print "Started scraping"
r = requests.get(main_url)
data = r.text
supaPocetna = BeautifulSoup(data, "html.parser")
book_number = 0

for imglink in supaPocetna.findAll("div", {"class" : "book_number"}):
		book_number = book_number + 1
		print "Book number is:" + str(book_number)

		
for url_range in range(1,book_number):
		urls = main_url + str(url_range)
		print "Entered Page " + str(urls)
		r = requests.get(urls)
		data = r.text
	 	supa = BeautifulSoup(data, "html.parser")
		for hadith in supa.findAll("div", {"class" : "text_details"}):
			ahit = hadith.text.encode('utf-8').decode('ascii', 'ignore')
			ahit = str(ahit)
			ahit.replace("<p>", "\n\n")
			ahit.replace("</p>", "\n\n")
			text_file = open(hadithFolder + "\\hadith" + str(url_range) + ".txt", 'a')
			text_file.write("%s\n\n" % (ahit))
			text_file.close()
