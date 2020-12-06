import re
def domain_name(url):
    if "//" in url:
        url = url.split('//')[1]
        if url.split('.')[0] == "www":
            url = url.split('.')[1]
            return url
        else:
            url = url.split('.')[0]
            return url
            
    else:
        if url.split('.')[0] == "www":
            url = url.split('.')[1]
            return url
        else:
            url = url.split('.')[0]
            return url
