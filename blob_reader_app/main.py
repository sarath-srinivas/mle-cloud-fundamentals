from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import json
import os


def get_folders(container):
    return [blob.name for blob in container.walk_blobs()]


def get_folder_contents(container, folder):
    return [blob.name for blob in container.list_blobs(name_starts_with=folder)]


module_loc = os.path.dirname(__file__)
secrets_file = os.path.join(module_loc, "secrets.json")

with open(secrets_file, "r") as f:
    secrets = json.load(f)

account_url = secrets["account_url"]
access_key = secrets["access_key"]

client = BlobServiceClient(account_url, credential=access_key)
container = client.get_container_client(container="flaskapp")

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<a href=/folders> FlaskApp Container listing </a>"


@app.route("/folders")
def list_folders():
    folders = get_folders(container)
    html = ""
    for folder in folders:
        html += f"<a href=/folder-content/{folder}> {folder} </a><br>"
    return html


@app.route("/folder-content/<folder>/")
def list_folder_contents(folder):
    contents = get_folder_contents(container, folder)
    html = ""
    for file in contents:
        html += f"{file}<br>"
    return html
