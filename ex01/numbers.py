def print_num():
    with open('numbers.txt') as handle:
        numbers = handle.readline().strip()
        for number in numbers.split(','):
            print(number)

if __name__ == '__main__':
    print_num()