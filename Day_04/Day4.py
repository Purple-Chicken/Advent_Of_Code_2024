import re
def main():
    with open('Day4.txt', 'r') as file:
        og_input = file.read().split("\n")
    print(og_input)
    search_count = 0
    search_count += horizontal_search(og_input, "XMAS")
    search_count += horizontal_search(og_input, "SAMX")
    #search_count += vertical_search(og_input, "XMAS")
    #search_count += vertical_search(og_input, "SAMX")
    #search_count += forward_diag_search(og_input, "XMAS")
    #search_count += forward_diag_search(og_input, "SAMX")
    #search_count += back_diag_search(og_input, "XMAS")
    #search_count += back_diag_search(og_input, "SAMX")
    print(f"XMAS appears in the word search {search_count} times.")

def horizontal_search(array, word):
    count = 0 #Local function count, not global count
    i = 0
    while i < len(array):
        count += len(re.findall(word, array[i]))
        print(f"Row {i+1} count: {count}")
        i += 1
    return count

def vertical_search(array,word):
    count = 0 #Local function count, not global count
    i=0
    while i < len(array[0]):
        print()
        i+= 1
    return count


if __name__ == "__main__":
    main()