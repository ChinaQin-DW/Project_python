# -- coding:utf-8 --
import csv
with open("G:\Project_china\Python_Project\Project_python\_temp\data_csv\data_1.csv","r") as csvfile:
    cf = csv.reader(csvfile)
    for i in cf:
        print(i)
        a=i[0]
        print(i[0][-3:])
        print(i[2])
        b=i
        csvFile = open("host_info.csv", "a",newline='')
        writer = csv.writer(csvFile)
        writer.writerow(b)
        csvFile.close()

