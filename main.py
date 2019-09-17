import requests
import xlwt
from bs4 import BeautifulSoup


url = 'https://www.yellowpages.com/search?search_terms=Coffee&geo_location_terms=Los+Angeles%2C+CA'
r = requests.get(url)

soup = BeautifulSoup(r.content)
links = soup.find_all('a')

g_data = soup.find_all('div', {"class": "info"})

wb = xlwt.Workbook()
ws = wb.add_sheet("test_sheet")

ws.write(0, 0, "Name")
ws.write(0, 1, "Phone")
ws.write(0, 2, "Street")
ws.write(0, 3, "State")

val = 1
for item in g_data:
    name = item.contents[0].find_all("a", {"class": "business-name"})[0].text
    phone = item.contents[1].find_all("div", {"class": "phone"})[0].text
    street = item.contents[1].findChildren("span", {"class": "street-address"})[0].text
    state = item.contents[1].findChildren("span", {"class": "locality"})[0].text.replace(',','')

    ws.write(val, 0, name)
    ws.write(val, 1, phone)
    ws.write(val, 2, street)
    ws.write(val, 3, state)
    val += 1

wb.save("restaurent_list.xls")