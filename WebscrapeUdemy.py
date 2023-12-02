from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
url = 'https://www.udemy.com/featured-topics/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(10)
page_source = driver.page_source
titles = []
soup = BeautifulSoup(page_source, 'lxml')
filtered_soup = soup.find(
    'table', class_='topic-list-collection_topic-list__UzEPd').tbody
rows = filtered_soup.find_all('tr')
for row in rows:
    title = row.a.get_text()
    titles.append(title)
d = {'Top Courses': titles}
df = pd.DataFrame(data=d)
print(df)
df.to_csv(r'C:\Users\Aditi\webscrapping\udemy_top_courses.csv', index=False)
