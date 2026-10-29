import re

def parse_and_sort_file(filename):
    relations_list = []
    try:
        with open(filename, "r") as file:
            contents = file.readline()
            while contents:
                relations_line = []
                for token in contents.split():
                    parts = re.split(r"([<>])", token)
                    if len(parts) == 3:
                        left, op, right = parts
                        try:
                            relations_line.append((int(left), op, int(right)))
                        except ValueError:
                            continue
                relations_list.append(relations_line)
                contents = file.readline()
    except FileNotFoundError:
        return


    result = 0
    for line in relations_list:
        result += determine_line_order(line)

    print("Checksum:", result)

def determine_line_order(line):
    numbers = set()
    graph = {}

    for left, op, right in line:
        numbers.add(left)
        numbers.add(right)
        if left not in graph: graph[left] = set()
        if right not in graph: graph[right] = set()

        if op == '<':
            graph[right].add(left)
        elif op == '>':
            graph[left].add(right)

    num_reachable = {}
    for number in numbers:
        visited = set()
        stack = [number]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                if curr in graph:
                    stack.extend(graph[curr] - visited)
        num_reachable[number] = len(visited) - 1

    sorted_list = sorted(numbers, key=num_reachable.__getitem__, reverse=True)

    return int("".join(map(str, sorted_list)))

if __name__ == "__main__":
    print("Part 1:")
    parse_and_sort_file("everybody_codes_e2026_q02_p1.txt")
    print("\nPart 2:")
    parse_and_sort_file("everybody_codes_e2026_q02_p2.txt")
    print("\nPart 3:")
    parse_and_sort_file("everybody_codes_e2026_q02_p3.txt")