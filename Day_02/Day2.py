def main():
    with open('Day2.txt' 'r') as file:
        og_table = file.read().rstrip()
    A = make_matrix(og_table)
    num_safe_reports=0
    


def make_matrix(input):
    temp_array = input.split('\n') #Splits lines of input into array
    formatted_array=[]
    for i in input:
        formatted_array.append(i.split().strip())# Splits each number in the line into its own array entry
    return formatted_array

if __name__ == "__main__":
    main()