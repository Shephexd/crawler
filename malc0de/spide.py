import requests as req
from bs4 import BeautifulSoup
import csv

writer = csv.writer(open('test.csv','w'))
i = 1
html_text = req.get("http://malc0de.com/database/index.php?"+str(i))

soup = BeautifulSoup(html_text.text,'html.parser')

table_rows = soup.select('tr.class1')
writer.writerow(['index','URL','IP','HASH'])

HEAD = True
data_list = list()
for i,row in enumerate(table_rows):
    if HEAD:
        HEAD = False
        continue

    data_list = [i for i in row.text.split('\n') if i is not '']
    print("%d th\t URL:%s\t IP:%s\t HASH: %s" %(i,data_list[1],data_list[2],data_list[-1]))
    writer.writerow([i,data_list[1],data_list[2],data_list[-1]])
