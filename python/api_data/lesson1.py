import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.github.com/repos/python/cpython/issues?per_page=10"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(type(data))
print(len(data))

df = pd.DataFrame(data)

df.head()

average_comments = df["comments"].mean()
print(average_comments)

plt.bar(df["number"].astype(str), df["comments"])

plt.xlabel("Issue Number")
plt.ylabel("Number of Comments")
plt.title("GitHub Issues — Comments")

plt.show()


most_commented = df.loc[df["comments"].idxmax()]

print(most_commented["number"])
print(most_commented["title"])
print(most_commented["comments"])


status_counts = df["state"].value_counts()
print(status_counts)


status_counts.plot(kind="bar")

plt.xlabel("Status")
plt.ylabel("Number of Issues")
plt.title("Open vs Closed Issues")
plt.show()



plt.figure(figsize=(10, 5))

plt.bar(df["number"].astype(str), df["comments"])

plt.xlabel("Issue Number")
plt.ylabel("Comments")
plt.title("Comments per GitHub Issue")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


