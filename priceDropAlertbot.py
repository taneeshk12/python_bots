rom tabnanny import check
import requests
import smtplib
from bs4 import BeautifulSoup
import time

a=input("enter url of product")
b=float(input("enter max price to get alert")
URL = a
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("span", {"class": "B_NuCI"}).get_text()

    price = float(soup.find("div", {"class": "_30jeq3 _16Jk6d"}).get_text()[1:].replace(',',''))
    if( price < b ): 
        sendmail()

def sendmail():
    '''Function called when the email needs to be sent '''
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo()
    server.starttls() 
    server.ehlo()
    
    server.login('yourmail@gmail.com', 'appPasswordFromGoogle')
    subject = 'Hey! Price fell down'
    body = 'Check the link ' + URL
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('sendermail@gmail.com', 'recievermail@gmail.com', msg)
        
    print('Email Sent')
    
    server.quit() 

while(True):
    check_price()
    time.sleep(60*60*24)
