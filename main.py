import pandas
import matplotlib.pyplot as plt
import csv

# rf = pandas.read_csv('/home/speedtest/result.csv', index_col='Timestamp')
# print(rf)
x = []
y = []

with open('result.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
            x.append(float(row[4]))
            y.append(float(row[7]))

plt.plot(x,y,linewidth=5)
plt.title("Network Download Speed Test")
plt.xlabel("Date")
plt.ylabel("Speed")
plt.show()