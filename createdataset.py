import csv
import pandas as pd
from bs4 import BeautifulSoup

def write_to_csv(filename):
    csvfile = csv.writer(open("chatdata.csv", "w"))
    csvfile.writerow(["date"])
    with open(filename) as fp:
        soup = BeautifulSoup(fp, 'lxml')
    dates = soup.findAll('div', {'class' : 'uiBoxWhite'})
    dates = soup.select('div.uiBoxWhite')
    for date in dates:
        data = date.select('div')[-1].text
        data = ''.join(data.split(',')[:2])
        csvfile.writerow([data])

def count_messages_bydate():
    df = pd.read_csv('chatdata.csv')
    df.groupby(df.date).size().to_csv("count.csv", header=True)
    ab = pd.read_csv('count.csv')
    ab['date'] = pd.to_datetime(ab.date)
    ab.sort_values('date').to_csv("sorted.csv", header=True)
