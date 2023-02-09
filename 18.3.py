import requests # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

# №1
# html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта Python
#
# tree = lxml.html.document_fromstring(html)
# title = tree.xpath('/html/head/title/text()')  # забираем текст тега <title> из тега <head> который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке. Её название и инструкции по отображению в браузере.
#
# print(title)  # выводим полученный заголовок страницы

# №2

# # создадим объект ElementTree. Он возвращается функцией parse()
# tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью HTML-парсера. Сам HTML — это то, что мы скачали и поместили в папку из браузера.
#
# ul = tree.findall('body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)
#
# # создаём цикл? в котором будем выводить название каждого элемента из списка
# for li in ul:
#     a = li.find('a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. Гиперссылки в HTML — это всегда тэг <a>.
#     print(a.text)  # из этого тега забираем текст — это и будет нашим названием

# №3

html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html',
                   lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью html парсера

ul = tree.findall(
    'body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath

# создаём цикл в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим где хранится название. У нас это тег <a>
    time = li.find('time')
    print(time.get('datetime'), a.text)  # из этого тега забираем текст - это и будет нашим названием


# # №4
# html = ''' <html>
#  <head> <title> Some title </title> </head>
#  <body>
#   <tag1> some text
#      <tag2> MY TEXT </tag2>
#    </tag1>
#  </body>
# </html>
# '''
#
# tree = lxml.html.document_fromstring(html)
#
# text = tree.xpath('/html/body/tag1/tag2/text()')
#
# print(text)