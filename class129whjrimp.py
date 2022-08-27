import csv 

dataset_1 = []
dataset_2 = []

with open("final.csv","r") as f :
    csv_reader = csv.reader(f)
    for row in csv_reader :
        dataset_1.append(row)

with open("archive_dataset_sorted1.csv","r") as f :
    csv_reader = csv.reader(f)
    #we are putting the sorted row ... basically appending the new,sorted row in the data set 
    for row in csv_reader :
        dataset_2.append(row)

header_1 = dataset_1[0]
#it will keep on working on the continued data : start from row 1 and continue till where the data ends
planet_data_1 = dataset_1[1:]

header_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

headers = header_1 + header_2
planet_data = []

for index , data_row in enumerate(planet_data_1):
    #merging the data (index is like the starting point)
    planet_data.append(planet_data_1[index]+planet_data_2[index])

#generating the file
with open("merged_dataset.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)


