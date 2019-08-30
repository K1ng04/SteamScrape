import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://store.steampowered.com/games/#p=0&tab=TopSellers"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
titles = soup.find_all('div', class_="tab_item_name")
prices = soup.find_all('div', class_='discount_final_price')
# x and y used to extract titles and prices w/ $
x = [price.get_text() for price in prices]
y = [title.get_text() for title in titles]
index = list(zip(y, x))

Table = pd.DataFrame(index, columns=['Title', "Price"])

# Removed Dollar Sign using below function


def reg(val):
    return val.replace("$", "")


T = [t.get_text() for t in titles]
# Applied Function to Table['Price'] and saved it to z
z = Table['Price'].apply(reg)
# Zipped the titles and new price(z)
zipped = list(zip(T, z))
# turned zipped into a DataFrame and applied column titles
List = pd.DataFrame(zipped, columns=['Title', "Price"]
                    ).reset_index().sort_values(by='Title', ascending=True).reset_index().drop_duplicates(subset='Title', keep=False, inplace=False)
# used reset_index() to fix indexing
del List['level_0']
del List['index']
# Deleted newly created level_0 and index column
print(List)
