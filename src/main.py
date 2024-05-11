import base64

from utils.infrastructure_setup import create_bucket
from utils.helper_functions import write_bucket
from utils.scraper import scrape

def handler(event, context):
    '''
    This function is triggered by a Pub/Sub message.
    When the function is triggered, it creates a bucket in GCS to store
    scraped data and writes the data to the bucket.

    Args:
        event (dict): Event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    '''
    # log the received pubsub message
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(f'This pipeline will scrape {pubsub_message}')

    # create a bucket in GCS
    bucket_name = 'gonzaga-scraper-bucket'
    create_bucket(bucket_name)

    # scrape website data
    # data = scrape(pubsub_message)

    # for testing purposes, the pubsub message (website to scrape) is used as data
    data = pubsub_message

    # write data to GCS
    write_bucket(bucket_name, data)
