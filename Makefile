scrape:
	echo "Scraping data from the web"
	python3 web_scraper/scraper.py

zip-scraper:
	cd src && zip -r ../bin/scraper.zip *

copy-scraper:
	gcloud storage cp bin/scraper.zip gs://gonzaga-scraper-bucket/scraper.zip