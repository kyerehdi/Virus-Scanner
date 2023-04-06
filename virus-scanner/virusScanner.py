import ctypes
import hashlib
import requests
from decouple import config
import os
import json

def getFileAsBytes(filePath):
    with open(filePath, "rb") as file:
        md5 = hashlib.md5()
        while True:
            data = file.read(8192)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def getFileReport(id, APIKEY):
    url = "https://www.virustotal.com/api/v3/files/"

    headers = {"accept": "application/json", "x-apikey": APIKEY}
    url = url + id
    response = requests.get(url, headers=headers)

    obj = response.json()
    if obj:
        result = obj["data"]["attributes"]["total_votes"]["malicious"]
        if result < 1:
            return "Scanner has not found Malware in this file."
        else:
            return "Scanner has found Malware in this file."
    else:
        return "Error occured while scanning file try again or try another file."


def uploadFile(filePath, APIKEY):
    url = "https://www.virustotal.com/api/v3/files"

    files = {"file": (filePath, open(filePath, "rb"))}
    headers = {"accept": "application/json", "x-apikey": APIKEY}

    response = requests.post(url, files=files, headers=headers)

    id = getFileAsBytes(filePath)
    if id:
        return getFileReport(id, APIKEY)
    else:
        return "Error in uploading the file"


def main(filePath):
    API_KEY = config("API_KEY")
    file_stats = os.stat(filePath)
    file_sizeMB = file_stats.st_size / (1024 * 1024)
    if file_sizeMB < 32:
       return uploadFile(filePath, API_KEY)
    else:
        return "File has to be less than 32MB";


if __name__ == "__main__":
    main()