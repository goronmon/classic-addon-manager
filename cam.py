from pathlib import Path
import requests

from paths import get_game_directory
from urls import get_latest_download_url

org = "AeroScripts"
repo = "QuestieDev"

url = get_latest_download_url(org, repo)
filename = f"addons/{Path(url).name}"

# If addon storage directory doesn't exist, create it

# Check if game directory has been saved already, otherwise search for it

# NOTE the stream=True parameter below
with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                # f.flush()