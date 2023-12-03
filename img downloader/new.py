from numpy.core.numeric import full
import pandas as pd
import urllib.request

def url_to_jpg(i, url, file_path):
    filename = 'image-{}.jpg'.format(i)
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)
    return None


FILENAME = 'allURL.csv'
FILE_PATH = 'images/'

urls = pd.read_csv(FILENAME)

for i, url in enumerate(urls.values):
    url_to_jpg(i, url[0], FILE_PATH)
