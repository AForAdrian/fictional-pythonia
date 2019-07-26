from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):

    try:
        #make a get request to a url and get the content
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during request to {0} : {1}'.format(url, str(e)))


def is_good_response(resp):
    #returns true for web pages
    content_type = resp.headers['Content-Type'].lower()
    return(resp.status_code==200
            and content_type is not None
            and content_type.find('html')>-1)

def log_error(e):
    #logs errors
    print(e )