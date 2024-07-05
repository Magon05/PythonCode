import requests
from bs4 import BeautifulSoup


# Запрос к веб-странице
response = requests.get('https://dom.gosuslugi.ru/#!/houses')

# Получение содержимого страницы
content = response.content

# Создание объекта BeautifulSoup для парсинга
soup = BeautifulSoup(content, 'html.parser')

# Нахождение всех ссылок на странице
links = soup.find_all('span', class_="house-card-address pull-left")

"""# Вывод найденных ссылок
result = ""
for i in links:
    result += str(i)

result = result.split('<a href="#" title=""></a>"')

with open("test.txt", "w") as f:
    for i in result:
        i.replace("<td>", "")
        f.write(i)
"""