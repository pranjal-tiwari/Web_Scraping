from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
print("Application Started..........")  
driver = webdriver.Chrome(executable_path="/Users/vedanttripathi/Desktop/chromedriver") 
 
  
 
driver.get("https://parivahan.gov.in/rcdlstatus/?pur_cd=101")

str = input("Enter Driving License No.: ")
driver.find_element_by_name("form_rcdl:tf_dlNO").send_keys(str)  
time.sleep(1)  

str = input("Enter DOB: ")
driver.find_element_by_name("form_rcdl:tf_dob_input").send_keys(str)  
time.sleep(1)  

str = input("Enter CaptchaID : ")
driver.find_element_by_name("form_rcdl:j_idt34:CaptchaID").send_keys(str)  
time.sleep(1)  


driver.find_element_by_name("form_rcdl:j_idt46").send_keys(Keys.ENTER)  
time.sleep(1)

import requests
import lxml.html
from lxml import etree
response = requests.get('https://parivahan.gov.in/rcdlstatus/?pur_cd=101')
#parser = etree.HTMLParser()
#byte_string = response.text
dictionary=dict()
tree = lxml.html.fromstring(response.content)[0]
elem_0=tree.xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[2]/td[1]/span')
elem_1= tree.xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[2]/td[2]')
elem_2=tree.xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[3]/td[1]/span')
elem_3=tree.xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[3]/td[2]')
elem_4=tree.xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[4]/td[1]/span')
elem_5=tree.xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[4]/td[2]')
elem_6=tree.xpath('//*[@id="form_rcdl:j_idt167:j_idt170"]')
elem_7=tree.xpath('//*[@id="form_rcdl:j_idt167_data"]/tr/td[2]')
dictionary[elem_0.text_content()]=elem_1.text_content()
dictionary[elem_2.text_content()]=elem_3.text_content()
dictionary[elem_4.text_content()]=elem_5.text_content()
dictionary[elem_6.text_content()]=elem_7.text_content()

import json

with open("scrap2.json", "wb") as outfile: 
    json.dump(dictionary, outfile)

driver.close()  
print("Successfully Done")


