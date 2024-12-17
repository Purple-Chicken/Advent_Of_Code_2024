def main():
    with open('Day2.txt', 'r') as file:
        A = make_matrix(file.read())
    num_safe_reports=0
    num_fixed_reports=0
    for line in A:
        if ascending(line) & difference(line) == True: #If both tests are safe
            num_safe_reports += 1
        else:
            temp_line = line.split()
            i=0
            while i < len(temp_line):
                del temp_line[i]
                temp_line = ' '.join(temp_line)
                if ascending(temp_line) & difference(temp_line) == True:
                    num_fixed_reports += 1
                    break
                i += 1
                temp_line = line.split()
    print(f"Number of Initial safe reports: {num_safe_reports}")
    print(f"Number of fixable safe reports: {num_safe_reports+num_fixed_reports}")
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