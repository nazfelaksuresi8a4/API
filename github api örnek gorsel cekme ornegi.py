import requests
import os
import re

owner = "kullaniciadi"
repo = "repoadi"
branch = "main"
path = "klasor"  # boş bırakmak için ""

api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}"

response = requests.get(api_url)
response.raise_for_status()

os.makedirs("gorseller", exist_ok=True)

for item in response.json():
    if item["type"] == "file" and re.search(r"\.(jpg|jpeg|png|gif|webp)$", item["name"], re.IGNORECASE):
        download_url = item["download_url"]
        img_data = requests.get(download_url).content
        
        with open(os.path.join("gorseller", item["name"]), "wb") as f:
            f.write(img_data)
