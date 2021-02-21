import requests
import mysql.connector
from re import search

url = "http://challenges.pwnedcr.com/challenges/5/?id="

for i in range(2197,1000):
    p_url = url+str(i)
    r =requests.get(p_url)
    p_status = str(r.status_code)
    p_text = r.text

    if search("PWNEDCR{", p_text):
        print("Found!: "+ p_url)
        break
    else:
        print(p_status + ": " + p_url)
