
def my_var():
    int_var = 42
    str_var = '42'
    float_var = 42.0
    bool_var = True
    list_var = [42]
    dict_var = {42: 42}
    tuple_var = (42,)
    set_var = set()

    print(int_var, 'has a type', type(int_var))
    print(str_var, 'has a type', type(str_var))
    print('quarante-deux has a type', type(str_var))
    print(float_var, 'has a type', type(float_var))
    print(bool_var, 'has a type', type(bool_var))
    print(list_var, 'has a type', type(list_var))
    print(dict_var, 'has a type', type(dict_var))
    print(tuple_var, 'has a type', type(tuple_var))
    print(set_var, 'has a type', type(set_var))

if __name__ == '__main__': 
    my_var()