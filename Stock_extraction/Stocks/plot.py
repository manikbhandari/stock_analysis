from csv import reader
from matplotlib import pyplot as pt

company_list = ['YHOO', 'GOOG', 'GOOGL', 'FB', 'TWTR', 'MSFT']

for company in company_list:
    with open(company+'14_17.csv','r') as f:
        data = list(reader(f))

    opening = [i[1] for i in data[1:]]
    highest = [i[2] for i in data[1:]]
    lowest = [i[3] for i in data[1:]]

    pt.title(company+' price by day')
    pt.xlabel('1-1-2014 to 27-1-2017')
    pt.ylabel('Price')
    pt.plot(range(len(opening)), opening, label="open")
    pt.plot(range(len(highest)), highest, label="high")
    pt.plot(range(len(lowest)), lowest, label="low")
    pt.legend()
    pt.show()