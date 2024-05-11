from google.cloud import storage

def write_bucket(bucket_name, data):
    '''
    Write data to a bucket in GCS

    Args:
        bucket_name (str): Name of the bucket to write to
        data (str): Data to write to the bucket

    Prints:
        str: Message indicating if the data was written successfully
    '''
    print('Writing data to GCS')
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    
    # remove existing data file if it exists
    if bucket.blob('data.txt').exists():
        bucket.blob('data.txt').delete()
    bucket.blob('data.txt').upload_from_string(data)

    print('Data written to GCS')