import requests
from bs4 import BeautifulSoup


# поиск в определённой зоне
url = "http://10.105.0.138/spr/department_other_workers.php?edit=0&do_name=МРСК&do_id=3"

# делаем запрос и получаем html
html_text = requests.get(url).text

# используем парсер lxml
soup = BeautifulSoup(html_text, 'lxml')

links = soup.find(class_="odd")

print(links)