import re

def main(filename):
    pattern = re.compile(r"(\w+)-(\d+)\s+(\d+)")
    votes = []

    # Open and read the file line by line
    with open(filename, "r") as file:
        for line in file:
            match = pattern.search(line)
            if match:
                standard_name = match.group(1)
                standard = [int(digit) for digit in str(match.group(2))]
                value = [int(digit) for digit in str(match.group(3))]
                votes.append((standard_name, standard, value))

    calculate_iso_votes(votes)

def calculate_iso_votes(votes):
    result_list = []
    for standard_name, standard, value in votes:
        value_int = int("".join(str(item) for item in value))
        if standard_name == "ISO":
            result_list.append(int(compute_value(standard, value)))
        elif standard_name == "ISO2":
            current_value = compute_value(standard, value)
            while value_int > 0:
                if int(current_value) == int(compute_value(standard, list(map(int, str(value_int-1))))):
                    current_value = 0
                    break
                value_int -= 1
            result_list.append(int(current_value))

    print(sum(result_list))

def compute_value(standard, value):
    value_length = len(value)
    standard_length = len(standard)
    count = len(value) - 1
    current_result = 0
    if standard_length < value_length:
        standard = standard[::-1]
        standard = [standard[i % standard_length] for i in range(value_length)]
        standard = standard[::-1]
    elif standard_length > value_length:
        standard = standard[-(value_length - standard_length):]
    for value_num, standard_num in zip(value, standard):
        current_result += value_num * (standard_num ** count)
        count -= 1
    return current_result

if __name__ == "__main__":
    main("everybody_codes_e2026_q03_p1.txt")
    main("everybody_codes_e2026_q03_p2.txt")
    main("everybody_codes_e2026_q03_p3.txt")