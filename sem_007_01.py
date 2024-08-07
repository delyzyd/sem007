from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Настройка пути к ChromeDriver
service = Service(r'C:\drivers\chromedriver.exe')  # Замените на фактический путь

driver = webdriver.Chrome(service=service)

# Открытие страницы
driver.get('https://example-ecommerce.com')

# Задержка для полной загрузки страницы
time.sleep(5)

# Извлечение содержимого страницы с помощью BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Найдите элементы, содержащие нужную информацию
products = soup.find_all('div', class_='product-item')

# Подготовка списка для хранения данных
data = []

# Извлечение данных из HTML
for product in products:
    title = product.find('h2', class_='product-title').text
    price = product.find('span', class_='product-price').text
    data.append({'title': title, 'price': price})

# Печать данных или сохранение в файл
for item in data:
    print(f"Title: {item['title']}, Price: {item['price']}")

# Закрытие драйвера
driver.quit()