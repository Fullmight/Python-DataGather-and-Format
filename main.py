# import Libraries
from selenium import webdriver
import unicodedata
import unicodecsv as csv
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

#setup driver
webCar = webdriver.Chrome('E:\Development\customDrivers\chromedriver_win32\chromedriver.exe')

#use Selenium to get the page.
webCar.get("https://na.wows-numbers.com/ships/")

table = webCar.find_element_by_css_selector("table")
print(table)
headers = ",".join([th.text for th in table.find_elements_by_xpath(".//thead/tr/td")])
print(headers)
entries = ";".join([et.text for et in table.find_elements_by_xpath(".//tbody/tr")])
print(entries)






# specify the url
#page_url = 'https://na.wows-numbers.com/ships/'

# query website and return html to variable 'page'
#page = urlopen(page_url)

# parse the html using beautiful soup and store in variable 'soup'
#soupObj = BeautifulSoup(page, 'html.parser')

#------------- Main content below here




#table = soupObj.find("table", attrs={'class': 'table'})
#tableTr = table.find('tr')
#tableTd = tableTr.find('td')
#tableTdText = tableTd.renderContents()
#tableTdText = tableTdText.strip()
#print(tableTdText)


#print("".join(soupObj.strings))


# remove the <div> of name and return its value
#siteName = soupObj.find('title')


#print title test
#print(siteName)

#for node in soupObj.findAll("td"):
#    print("".join(node.findAll(text=True)))

# get index price

# Whatever your key information is, it goes in here. create more
# in the same Vein if needed.
#coreDataVar = soupObj.find('tbody', {"": ""})

#print(coreDataVar)
#if coreDataVar:
#    price = coreDataVar.get_text(separator=':').encode("utf-8")
    #print(price)

#finalList = price.splitlines()

#for z in range(len(finalList)):
#    interIter = finalList[z]
#    finalList[z] = interIter.decode("utf-8")#.replace(',','',1)
#    print(finalList[z])
    #for i, c in enumerate(finalList[z]):
    #   if c.isdigit():
    #      finalList[z] = finalList[z][:i] + ' ' + finalList[z][i:]
    #     break
    #



#for y in finalList:
    #print(y)

#append Data to a CSV file
with open('index.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file, encoding='utf-8')
    #dictW = csv.DictWriter(csv_file, encoding='utf-8')
    #dictW.writeheader([headers])
    writer.writerow([entries])
    #for x in finalList:
    #    writer.writerow([x, datetime.now()])

webCar.quit()

#Opens csvFormat.py and runs it; formatting the CSV file automagically
#exec(open("./csvFormat.py").read())
