import re
def main():
    with open('Day4.txt', 'r') as file:
        og_input = file.read().split("\n")
    #print(og_input)
    xword = make_array(og_input)
    search_count = 0
    search_count += horizontal_search(og_input, "XMAS")
    search_count += horizontal_search(og_input, "SAMX")
    print(f"XMAS appears in the word search {search_count} times horizontally.")
    search_count += vertical_search(xword, "XMAS")
    search_count += vertical_search(xword, "SAMX")
    print(f"XMAS appears in the word search {search_count} times horizontally and vertically.")
    #search_count += forward_diag_search(xword, "XMAS")
    #search_count += forward_diag_search(xword, "SAMX")
    #search_count += back_diag_search(xword, "XMAS")
    #search_count += back_diag_search(xword, "SAMX")
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
            count += len(re.findall(word, ''.join(temp_array)))
            print(count)
            j += 1
        i += 1
    return count

def forward_diag_search(array, word):
    count = 0

    return count



if __name__ == "__main__":
    main()