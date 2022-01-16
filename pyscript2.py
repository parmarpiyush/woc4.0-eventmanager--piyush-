import csv   #pandas library


#for reading from the csv file :
with open('data.txt','r') as data_file:  #this open a file in read mode
    csv_reader = csv.reader(data_file)  #this will store file in csv_reader mode

#print(csv_reader) doesn't work because it's object
    for line in csv_reader:  #for iterating line by line
        print(line)
        #print(line[0])  this will print column 1
        #print(line[1]) this will print column 2



#for writing into some other file by some other sepersted symbol

with open('data.txt','r') as data_file:  #for read data from one file
    csv_reader = csv.reader(data_file)

    with open('new_data.csv','w') as new_data_file:   #for store data to some new file
        csv_writer = csv.writer(new_data_file, delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)
