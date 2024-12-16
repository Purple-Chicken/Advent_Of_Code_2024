import re
def main():
    with open('Day3.txt', 'r') as file:
        og_input = file.read()
    mul_list = re.findall(r"mul\(+\d{1,3}+,+\d{1,3}+\)", og_input)
    print(f"Multiplication sum: {add_mul(mul_list)}")
    print(f"Enabled Multiplication sum: {add_mul(enabled(og_input))}")
def enabled(input_str):
    temp_list = re.sub(r"don't\(\)", "N", input_str) # Converts don't() to N
    temp_list = re.sub(r"do\(\)", "Y", temp_list) #Converts a do() to a Y (for easier regex next step)
    temp_list = re.sub(r"N+[^Y]*+Y", "", temp_list) #Replaces a don't() ... do() pair with blank space
    return re.findall(r"mul\(+\d{1,3}+,+\d{1,3}+\)", temp_list)
def add_mul(mul_list):
    mul_sum = 0
    for i in mul_list:
        a=""
        b=""
        a,b = i.lstrip("mul(").rstrip(")").split(",")
        mul_sum += mul(a,b)
    return mul_sum
def mul(a,b):
    return int(a)*int(b)
if __name__ == "__main__":
    main()