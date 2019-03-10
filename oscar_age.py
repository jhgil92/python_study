def oscar_age():
    """# 작성조건
1. `oscar_age_female.csv` 및 `oscar_age_male.csv` 파일을 읽어서 
   하나의 파일로 merge 하세요(`oscar_age.csv`).
2. `Name` 과 `Movie` 컬럼 사이에 `Gender` 컬럼을 추가한 후, `Female` 또는 `Male` 값을 넣으세요.
3. `Year` 컬럼 값으로 오름차순 정렬하고, `Index` 값을 새로 작성하세요."""
    
    # open csv files
    f1 = open("oscar_age_female.csv")
    f2 = open("oscar_age_male.csv")
    fw = open("oscar_age.csv", "w")
    
    # set list to store the values
    data = []
    
    # read female.csv
    index = 0
    for line in f1:
        temp = line.strip().split(",")
        if(index==0):
            temp.insert(4, " \"Gender\"")
            data.append(temp)
        else:
            temp.insert(4, " \"Female\"")
            data.append(temp)
        index += 1

    # read male.csv
    f2.readline()
    for line in f2:
        temp = line.strip().split(",")
        temp.insert(4, " \"Male\"")
        data.append(temp)
        
    for line in data:
        if(len(line)==2):
            data.remove(line)
        
    data.sort(key=lambda x: x[1])
    
    # write csv
    index = 0
    for line in data:
        if(index==0):
            fw.write(str(",".join(line))+"\n")
        else:
            fw.write(str(index)+","+ ",".join(line[1:])+"\n")
        index += 1
        
    # close the files
    f1.close()
    f2.close()
    fw.close()

if __name__ == "__main__":
    oscar_age()