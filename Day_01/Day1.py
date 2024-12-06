
def main():
    with open('Day1.txt', 'r') as file:
        og_list = file.read().rstrip()
    print(og_list)
    list_a,list_b = split_code(og_list) #Returns txt into 2 sorted lists
    print(f"Difference: {find_diff(list_a,list_b)}")
    print(f"Similarity: {find_similar(list_a,list_b)}")

def find_diff(a,b):
    difference=0
    for index, i in enumerate(a):
        local_diff = abs(int(a[index])-int(b[index]))
        difference += local_diff
    return difference

def find_similar(a,b):
    total_similarity = 0
    for i in a: #For every ID in list A
        temp_similar = b.count(i)   #Count howe many times it shows up in B
        total_similarity += int(i)*int(temp_similar2) #Add that to running total
    return total_similarity

def split_code(str_1):
    a=[] #Create empty array
    b=[]
    temp_array = str_1.split('\n') #Converts str into full array
    for line in temp_array:  #Splits temp_array line by line. temp1 goes to a, temp2 goes to b
        temp1,temp2 = line.split("   ")
        a.append(temp1)
        b.append(temp2)
    a = sorted(a) #Sorts the functions in ascending order
    b = sorted(b)
    return a,b



if __name__ == "__main__":
    main()
