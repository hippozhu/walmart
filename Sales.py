from collections import namedtuple
import csv
import cPickle as pickle
from datetime import date

Sale = namedtuple('Sale', ['store', 'dept', 'date', 'weekly_sale', 'isholiday'])
def readSalesData():
  reader = csv.reader(open('train.csv'))
  salelist = []
  reader.next()
  for row in reader:
    salelist.append(Sale(int(row[0]), int(row[1]), date(*[int(x) for x in row[2].split('-')]), float(row[3]), bool(row[4])))
  return salelist
  #pickle.dump(salelist, open('SalesList', 'wb'))


if __name__ == '__main__':
  #sl = pickle.load(open('SalesList'))
  sl = readSalesData()

