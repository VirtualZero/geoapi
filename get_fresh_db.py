import requests
import gzip

GEO_DB_LOCATION = 'geoapi/geo_db/GeoLite2-City.mmdb'
DOWNLOAD_GEO_DB_URL = 'http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz'

request = requests.get(
    DOWNLOAD_GEO_DB_URL,
    stream=True
)

gzip_file_location = f'{GEO_DB_LOCATION}.tar.gz'

with open(gzip_file_location, 'wb') as f:
        for chunk in request.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()

with open(GEO_DB_LOCATION, 'wb') as f:
        with gzip.open(gzip_file_location, 'rb') as g:
            f.write(g.read())
