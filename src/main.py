import base64

from gcp_utils.infrastructure_setup import create_bucket
from gcp_utils.helper_functions import write_bucket

def handler(event, context):
    # log the received pubsub message
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    # create a bucket in GCS
    bucket_name = 'gonzaga-scraper-bucket'
    create_bucket(bucket_name)

    # write data to GCS
    write_bucket(bucket_name, pubsub_message)
