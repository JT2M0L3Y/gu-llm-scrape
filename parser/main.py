import base64

from utils.helper_functions import read_bucket

def handler(event, context):
    '''
    This function is triggered by a change in the GCS bucket.
    When the function is triggered, it reads the data from the bucket
    and logs the data.

    Args:
        event (dict): Event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    '''
    # read data from GCS
    bucket_name = 'gonzaga-scraper-bucket'
    data = read_bucket(bucket_name)

    # log data
    print(data)
