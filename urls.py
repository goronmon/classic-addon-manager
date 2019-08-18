import json
from pathlib import Path
import requests

def get_latest_download_url(org, repo):
    base_url = "https://github.com/"

    api_url = f"https://api.github.com/repos/{org}/{repo}/releases/latest"

    response = requests.get(api_url)
    json_data = json.loads(response.content)
    json_string = json.dumps(json_data)

    tag_name = json_data['tag_name']
    filename = json_data['assets'][0]['name']

    download_url = base_url + f"{org}/{repo}/releases/download/{tag_name}/{filename}"

    return download_url
