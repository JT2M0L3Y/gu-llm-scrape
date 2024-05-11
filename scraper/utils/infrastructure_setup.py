from google.cloud import storage

def create_bucket(bucket_name):
    '''
    Create a new bucket in GCS if it doesn't exist

    Args:
        bucket_name (str): Name of the bucket to create

    Prints:
        str: Message indicating if the bucket was created or already exists
    '''
    print(f'Creating bucket {bucket_name}')
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    bucket.location = 'us-west1'
    bucket.storage_class = 'STANDARD'

    if not bucket.exists():
        bucket.create()
        print(f'Bucket {bucket_name} created')
    else:
        print(f'Bucket {bucket_name} already exists')
