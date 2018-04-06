import csv

import pandas as pd

i =0
data = []
with open('hackathon.csv', 'rt', encoding='utf8') as csvfile:
   spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
   for row in spamreader:
       xx = "".join(row)
       record = xx.split('|')
       data.append(record)
       if(i%1000 == 0):
           print(i)
       i+=1

labels = data.pop(0)
dataframe = pd.DataFrame.from_records(data, columns=labels)
xx =1