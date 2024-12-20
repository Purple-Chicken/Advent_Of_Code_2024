import re
def main():
    with open('Day4.txt', 'r') as file:
        og_input = file.read().split("\n")
    #print(og_input)
    xword = make_array(og_input)
    search_count = 0
    search_count += horizontal_search(og_input, "XMAS")
    search_count += horizontal_search(og_input, "SAMX")
    #print(f"XMAS appears in the word search {search_count} times horizontally.")
    search_count += vertical_search(xword, "XMAS")
    search_count += vertical_search(xword, "SAMX")
    print(f"XMAS appears in the word search {search_count} times horizontally and vertically.")
    search_count += forward_diag_search(tall_array(xword, 1), "XMAS")
    search_count += forward_diag_search(tall_array(xword, 1), "SAMX")
    search_count += back_diag_search(tall_array(xword, 0), "XMAS")
    search_count += back_diag_search(tall_array(xword, 0), "SAMX")
    print(f"XMAS appears in the word search {search_count} times.")
def make_array(input_str):
    return [list(i) for i in input_str]

def horizontal_search(array, word):
    count = 0 #Local function count, not global count
    i = 0
    while i < len(array):
        count += len(re.findall(word, array[i]))
        i += 1
    return count

def vertical_search(array,word): 
    count = 0 #Local function count, not global count
    i=0
    while i < len(array[0]):
        temp_array = []
        j=0
        while j < len(array[0]):
            temp_array.append(array[i][j])
            count += len(re.findall(word, ' '.join(temp_array)))
            j += 1
        i += 1
    return count

def back_diag_search(array, word): #Searches in backslashes \\\\\\\\
    count = 0
    i=0
    split_val= (len(array)-1)/2
    for k in array:
        print(k)
    while i < (len(array)+1)/2:
        temp_array = []
        j=0
        while j < len(array[0]):
            temp_array.append(array[i+j][j])
            j += 1
        print(temp_array)
        count += len(re.findall(word, ''.join(temp_array)))
        i += 1
    while i < len(array):
        temp_array = []
        j=0
        while j < len(array)-i:
            temp_array.append(array[i+j][j])
            #print(f"Appending: array[{i+j}][{j}] = {array[i+j][j]}")
            j += 1
        print(temp_array)
        count += len(re.findall(word, ''.join(temp_array)))
        i += 1
    return count

def tall_array(array, mode): #Adds m-1 * n rows below original array. Index now covers all diags instead of just half.
    m = len(array)
    temp_array = []
    empty_str = ["."] * len(array[0])
    i=1
    if mode == 1:
        for j in array:
            temp_array.append(j)
        while i < m:
            temp_array.append(empty_str)
            i += 1
        return temp_array
    elif mode == 0: #0 is blankspace on top, 1 is blankspace on bottom
        while i < m:
            temp_array.append(empty_str)
            i += 1
        for j in array:
            temp_array.append(j)
        return temp_array
    else:
        return array

def forward_diag_search(array, word): #Searches in forwardslashes ///
    count = 0
    i=len(array)-1
    while i > 0:
        temp_array = []
        j=0
        while j < (len(array[0])):
            temp_array.append(array[i-j][j])
            j += 1
        print(temp_array)
        count += len(re.findall(word, ''.join(temp_array)))
        i += -1
    return count

if __name__ == "__main__":
    main()