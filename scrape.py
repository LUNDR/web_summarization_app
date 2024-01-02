import requests
from bs4 import BeautifulSoup
import os
from google.cloud import storage

# storage_client = storage.Client.from_service_account_info('/terraform-key.json')

# Authentication

from google.oauth2 import service_account

key_path = "terraform-key.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = storage.Client(credentials=credentials, project=credentials.project_id)



# Specify the URL of the website you want to scrape
url = "https://www.betterup.com/blog/life-coaching"

# Scrape the website using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract the content you want to store
content = soup.find_all("p")

print(content)

# Create a Google Cloud Storage client
storage_client = storage.Client()

# Create a bucket or select an existing one
# Create a new bucket named 'my-bucket'
bucket = storage_client.bucket('web_sum_solid_altar')
bucket.create()


# Create a file path in the bucket
filename = "betterup.html"
blob = bucket.blob(filename)

# Write the scraped content to a file in the bucket
blob.upload_from_string(str(content))