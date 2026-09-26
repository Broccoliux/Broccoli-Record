import requests
import pandas as pd
import matplotlib.pyplot as plt

print("Everything works!")



url = "https://api.github.com"

response = requests.get(url)

print(response.status_code)
print(response.json())
