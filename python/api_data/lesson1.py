import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.github.com/repos/python/cpython/issues?per_page=10"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(type(data))
print(len(data))
