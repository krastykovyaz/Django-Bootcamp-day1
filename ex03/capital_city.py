import sys

def cap_city():
    states = {
        "Oregon" : "OR", 
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = { 
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    
    n = len(sys.argv)
    if  n == 2 and sys.argv[1] not in states:
        print('Unknown state')
    if 0 < n:
        i = 1
        for item in sys.argv[1:]:
            if item not in states:
                if i + 1 < n:
                    tmp_item = item + ' ' + sys.argv[i + 1]
                    if tmp_item not in states:
                        exit(0)
            i += 1
        input_state = ' '.join(sys.argv[1:])
        if input_state in states.keys():
            if input_state in states:
                print(capital_cities[states[input_state]])

if __name__ == "__main__":
    cap_city()