import json
import logging
import os
from pathlib import Path
from urllib.request import urlopen, Request

logger = logging.getLogger(__name__)

types = {'image/jpeg', 'image/png'}

def get_links(client_id, url):
    headers = {'Authorization': 'Client-ID {}'.format(client_id)}
    req = Request(url', headers=headers, method='GET')
    with urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    print(data['data'])
    return [item['link'] for item in data['data'] if 'type' in item and item['type'] in types]


def download_link(directory, link):
    download_path = directory / os.path.basename(link)
    with urlopen(link) as image, download_path.open('wb') as f:
        f.write(image.read())
    logger.info('Downloaded %s', link)


def setup_download_dir():
    download_dir = Path('images')
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir


def main():
    url = 'https://www.example.com'
    
    data = get_links(CLIENT_ID, url)
    print('=======')
    print(data)

if __name__ == '__main__':
    main()
