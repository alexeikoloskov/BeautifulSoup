from bs4 import BeautifulSoup
import requests


URL = requests.get('https://mainfin.ru/currency/usd/rostov-na-donu')
parse = BeautifulSoup(URL.text, 'html.parser')

Data = parse.find('span',{'class':'float-convert__btn'})
RATE = float(Data.text)

s = input("Введите сумму в USD ")

def USD(s):
    try:
        s = float(s)
    except:
        s=0
    return (RATE*s)


print(round(USD(s),1), 'рублей')