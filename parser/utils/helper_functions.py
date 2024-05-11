from google.cloud import storage

def read_bucket(bucket_name):
    '''
    This function reads the data from the GCS bucket.

    Args:
        bucket_name (str): The name of the GCS bucket.

    Returns:
        str: The data in the GCS bucket.
    '''
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob('data.txt')
    data = blob.download_as_string()
    return data.decode('utf-8')