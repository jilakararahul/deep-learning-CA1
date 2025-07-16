import json
import requests
import os
from urllib.parse import urlparse

# Load the HAR file
with open("lexica.har", "r", encoding="utf-8") as f:
    har_data = json.load(f)

# Make output directory
os.makedirs("har_images", exist_ok=True)

count = 1
for entry in har_data["log"]["entries"]:
    mime_type = entry.get("response", {}).get("content", {}).get("mimeType", "")
    url = entry.get("request", {}).get("url", "")
    status = entry.get("response", {}).get("status", 0)
    resource_type = entry.get("_resourceType", "")

    # Check it's a valid image
    if mime_type.startswith("image/") and resource_type == "image" and status == 200:
        try:
            ext = mime_type.split("/")[-1]
            ext = ".jpg" if ext == "jpeg" else f".{ext}"
            filename = os.path.join("har_images", f"har_image_{count}{ext}")
            response = requests.get(url, timeout=10)
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"✅ Downloaded {filename}")
            count += 1
        except Exception as e:
            print(f"❌ Failed to download {url} — {e}")
