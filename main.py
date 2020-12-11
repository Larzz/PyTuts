# basic types and variable instantiation
def print_var():
    string_array = ['name', 'name2']
    print(string_array)


print_var()


def function_with_argument(str1, str2):
    print(str1 + str2)


function_with_argument('22', str(22))
function_with_argument(int('2'), int('2'))


def default_argument(name, age):
    print('hello my name is ', name, ' and my is age', age)


default_argument('nick', 2)


def default_def_with_argument(name='s', age='0'):
    print('hello my name is ', name, 'and my age is', age)


default_def_with_argument()


def keyword_argument(name='S', age=1):
    print('hello my name is ', name, 'and my age is', age)


keyword_argument(age=2, name='susan')


def infinite_argument(*people):
    for person in people:
        print('the person is ', person)


infinite_argument('name', 'name2', 'name3')


def return_values_from_function(val):
    return val


print(return_values_from_function('2'))
print(return_values_from_function('3'))


def return_values_from_calculations(val):
    if val != 2:
        val = 2
    return val


print(return_values_from_calculations(2) + return_values_from_calculations(3))
print(return_values_from_calculations(22) + return_values_from_calculations(2))


def conditional_statement(val):
    if val is str:
        val = int(str)
    return val


print(conditional_statement('2'))


def conditional_statement_with_elif(val):
    if val:
        return 'item is good'
    elif not val:
        return 'item is empty'
    else:
        return 'either of the is not true'


print(conditional_statement_with_elif(2))


def for_loop(*people):
    for person in people:
        print('person is', person)
    return True


for_loop('nick', 'jonas')


def while_loop():
    run = True
    current = 1
    while run:
        if current == 10:
            return False
        else:
            current += 1
            print(current)


print(while_loop())


