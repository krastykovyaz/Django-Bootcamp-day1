import sys

def cap_state(states, capital_cities, input_cap):
    for k,v in capital_cities.items():
        # print(input_cap, v.lower())
        if input_cap == v.lower():
            for state, cut_vers in states.items():
                if cut_vers == k:
                    return (state, v)

def cap_city(states, capital_cities, input_state):
    for k,v in states.items():
        # print(input_state, k.lower())
        if input_state == k.lower():
            return (k, capital_cities[states[k]])

def parse_cap():
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
    if n > 0:
        comma_str = sys.argv[1]
        item_list = comma_str.split(',')
        for item in item_list:
            item_strip = item.strip()
            item_fix = item.strip().lower()
            if item_fix != '':
                cap = cap_city(states, capital_cities, item_fix)
                state = cap_state(states, capital_cities, item_fix)
                if cap != None:
                    print(cap[1], 'is the capital of', cap[0])
                elif state != None:
                    print(state[1], 'is the capital of', state[0])
                else:
                    print(item_strip, 'is neither a capital city nor a state')
            # if item == 'Trenton':
            #     break





if __name__ == '__main__':
    parse_cap()