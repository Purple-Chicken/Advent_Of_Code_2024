def main():
    with open('Day2.txt', 'r') as file:
        A = make_matrix(file.read())
    num_safe_reports=0
    for line in A:
        if ascending(line) & difference(line) == True: #If both tests are safe
            num_safe_reports += 1
    print(f"Number of Initial safe reports: {num_safe_reports}")
def ascending(line):
    i=0
    line = line.split()
    try:
        direction = (int(line[0])-int(line[1]))/abs(int(line[0])-int(line[1]))
    except ZeroDivisionError:
        return False
    else: 
        while i < len(line)-1:
            try:   
                temp_dir = (int(line[i])-int(line[i+1]))/abs(int(line[i])-int(line[i+1]))
            except ZeroDivisionError:
                return False
            else:
                if temp_dir != direction:
                    return False
            i += 1
        return True
def difference(line):
    i=0
    line = line.split()
    while i < len(line)-1:
        if abs(int(line[i])-int(line[i+1])) > 3:
            return False
        i += 1
    return True
def make_matrix(input):
    return input.split('\n') #Splits lines of input into array
if __name__ == "__main__":
    main()