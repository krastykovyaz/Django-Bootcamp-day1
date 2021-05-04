import sys

def cap_state():
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
    if  n == 2 and sys.argv[1] not in capital_cities.values():
        print('Unknown capital city')
    # if 0 < n:
        i = 1
        for item in sys.argv[1:]:
            if item not in capital_cities.values():
                if i + 1 < n:
                    tmp_item = item + ' ' + sys.argv[i + 1]
                    if tmp_item not in capital_cities.values():
                        exit(0)
            i += 1
    input_cap = ' '.join(sys.argv[1:])
    if input_cap in capital_cities.values():
        for k,v in capital_cities.items():
            if input_cap == v:
                for state, cut_vers in states.items():
                    if cut_vers == k:
                        print(state)

                        
if __name__ == "__main__":
    cap_state()