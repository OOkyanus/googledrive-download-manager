
import requests 

def url2downloadlink(url):
    url_tokens = url.split('/')
    d_idx = url_tokens.index('d')
    uid=url_tokens[d_idx+1]
    return "https://drive.google.com/uc?export=download&id="+uid

def gd_download(url,file_name=None):
    assert file_name is not None

    url=url2downloadlink(url)
    response = requests.get(url)
    open(file_name, "wb").write(response.content)

if __name__=='__main__':
    gd_download('google drive shareable link','my_file.extention')