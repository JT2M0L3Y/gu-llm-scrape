def write_data():
    from google.cloud import storage
    from urllib import request

    url = 'https://www.gonzaga.edu'
    client = storage.Client()
    bucket = client.get_bucket('gonzaga-scraper-bucket')
    
    # write data to GCS
    blob = bucket.blob('data.txt')

    with request.urlopen(url) as response:
        html = response.read()
        blob.upload_from_string(html)

    print('Data written to GCS')
