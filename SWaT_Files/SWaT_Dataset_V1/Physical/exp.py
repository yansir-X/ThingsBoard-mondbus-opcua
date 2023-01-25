import csv
c=0
with open('SWaT_Dataset_Attack_v0.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(row[1])
        c+=1
        if c==5:
            break