calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(h):
    count_calls()
    string = (h)
    h = (len(string), string.upper(), string.lower())
    return h
def is_contains(n, m):
    count_calls()
    string = (n.lower())
    my_list = (m)
    list_to_search = []
    for name in my_list:
        list_to_search.append(name.lower())
    sum1 = 0
    for i in range(0, len(list_to_search)):
        if list_to_search[i] == string:
            sum1 += 1
        else:
            i += 1
    if sum1 > 0:
        print(True)
    else:
        print(False)
print(string_info('Capybara'))
print(string_info('Armageddon'))
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)