file=open("CSV's/stud_info.csv",'r')
info_dataset=[]
while True:
    data=file.readline()
    if data:
        info_dataset.append(data.replace("\n", "").split(','))        
    else:
        break
print(info_dataset)