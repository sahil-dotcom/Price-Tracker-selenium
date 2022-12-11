import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import smtplib
import local_settings
from gmail.gmail import gmail

os.environ['PATH'] += r""
driver = webdriver.Chrome()
url="https://www.amazon.in/Samsung-500GB-Internal-Solid-MZ-V8V500/dp/B08THW4S3T/ref=sr_1_6?crid=39PIMQIM1C8FC&keywords=nvme+ssd&qid=1669819615&qu=eyJxc2MiOiI1LjIyIiwicXNhIjoiNC44MyIsInFzcCI6IjQuMDcifQ%3D%3D&sprefix=nvm%2Caps%2C422&sr=8-6"

def alert_me(url,name, priceWanted):

    server = smtplib.SMTP('smtp.gmail.com',587)
    
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login(local_settings.Email_ID,local_settings.Password)
    
    subject = 'Price fell down for '+name   
    body = 'Buy it now here: '+url   
    msg = f"Subject:{subject}\n\n{body}".encode('utf-8').strip()
    
    server.sendmail(local_settings.Sender,local_settings.Receiver, msg)
    print('Email alert sent')    
    server.quit()

def trackprice(url, priceWanted):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    driver.get(url)
    try:
        name = driver.find_element(By.ID, "productTitle")
        price = float(driver.find_element(By.CLASS_NAME, "a-price-whole").text[1:].replace(",",""))
        
        if (price == priceWanted):
            alert_me(url, name, priceWanted)
    except:
            print("no details found on this product")
    return 1
print(trackprice(url, 4949))


