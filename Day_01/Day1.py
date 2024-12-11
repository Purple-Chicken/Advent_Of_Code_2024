def main():
    with open('Day1.txt', 'r') as file:
        og_list = file.read().rstrip()
    #print(og_list)
    a,b = split_code(og_list) #Returns txt into 2 sorted lists
    print(f"Difference: {find_diff(a,b)}")
    print(f"Similarity: {find_similar(a,b)}")

def find_diff(a,b):
    c=0
    for index, l in enumerate(a):
        t_1 = abs(int(a[index])-int(b[index]))
        c = c + t_1
    return c

def find_similar(a,b):
    t_1 = 0
    for i in a:
        t_2 = b.count(i)
        t_1 += int(i)*int(t_2)
    return t_1

def split_code(str_1):
    a=[]
    b=[]
    nlines = str_1.count('\n')
    length = str_1.split('\n')
    for line in length: 
        temp1,temp2 = line.split("   ")
        a.append(temp1)
        b.append(temp2)
    a = sorted(a)
    b = sorted(b)
    return a,b

if __name__ == "__main__":
    main()