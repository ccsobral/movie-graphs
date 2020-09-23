import urllib.request
import urllib.error

for name in ['basics', 'ratings', 'episode']:
    url = f'https://datasets.imdbws.com/title.{name}.tsv.gz'
    file_name = f'./data/{name}.tsv.gz'
    try:
        request = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print(f'Could not find {url}, is IMDB down?')
        print(e.reason)
    else:
        with open(file_name, 'wb') as f:
            f.write(request.read())
        print(f'Successfully downloaded {url}.')
