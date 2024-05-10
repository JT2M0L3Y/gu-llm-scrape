scrape:
	echo "Scraping data from the web"

zip-scraper:
	zip -r bin/scraper.zip src/

copy-scraper:
	gcloud storage cp bin/scraper.zip gs://gonzaga-scraper-bucket/scraper.zip