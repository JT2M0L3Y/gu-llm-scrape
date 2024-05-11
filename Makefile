scrape:
	echo "Scraping data from the web"
	python3 web_scraper/scraper.py

zip-scraper:
	cd scraper && zip -r ../bin/scraper.zip *

zip-parser:
	cd parser && zip -r ../bin/parser.zip *

copy-scraper:
	gcloud storage cp bin/scraper.zip gs://gonzaga-scraper-bucket/scraper.zip

copy-parser:
	gcloud storage cp bin/parser.zip gs://gonzaga-scraper-bucket/parser.zip