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
    result = obj["data"]["attributes"]["total_votes"]["malicious"]
    if result < 1:
        return "Scanner has not found Malware in this file."
    else:
        return "Scanner has found Malware in this file."


def uploadFile(filePath, APIKEY):
    url = "https://www.virustotal.com/api/v3/files"

    files = {"file": (filePath, open(filePath, "rb"))}
    headers = {"accept": "application/json", "x-apikey": APIKEY}

    response = requests.post(url, files=files, headers=headers)

    id = getFileAsBytes(filePath)
    getFileReport(id, APIKEY)


def main():
    API_KEY = config("API_KEY")
    filePath = "C:/Users/Derrick/Documents/mongo.txt"
    file_stats = os.stat(filePath)
    print(file_stats)
    file_sizeMB = file_stats.st_size / (1024 * 1024)
    print(file_sizeMB)
    if file_sizeMB < 32:
        uploadFile(filePath, API_KEY)
    print(getFileAsBytes(filePath))


if __name__ == "__main__":
    main()