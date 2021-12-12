import sys

def get_items():
    title = '' # str
    # keys = [each_string.capitalize() for each_string in items.keys()]
    # print(f'{keys[0]}\t{keys[1]}\t{keys[2]}\t{keys[3]} (PLN)')
    for key, values in items.items():
        title += f'{key.title()}\t'

    print(f'{title}(PLN)')
    print('----\t--------\t----\t----------\t-----')
    get_list()

def get_list():
    x = items['name']
    for i in x:
        # print(f"{items['name'][x.index(i)]}\t{items['quantity'][x.index(i)]}"
        #       f"\t{items['unit'][x.index(i)]}\t{items['unit_price'][x.index(i)]}")
        try:
            print('{a:<10}{b: <10}{c: <10}{d: <10}'.format(a=f"{items['name'][x.index(i)].title()}",
                                                           b=f"{items['quantity'][x.index(i)]}",
                                                           c=f"{items['unit'][x.index(i)]}",
                                                           d=f"{items['unit_price'][x.index(i)]}"))
        except:
            print("errors items")

def users_add_list():
    try:
        items['name'].append(input('please name items').lower())
        items['quantity'].append(int(input('please write quantity')))
        items['unit'].append(str(input('please write KG or L or ...')))
        items['unit_price'].append(float(input('please write price ')))
    except:
        print("error")
    else:
        pass

def shell():
    x = items['name'].index(input('please write item').lower())
    items['quantity'][x] -= int(input("please write quantity "))



def help_users():
    help_user = 'please write comands = exit \n' \
                'or\n' \
                'please write comands = show\n' \
                'or\n' \
                ''
    print(help_user)

items = {'name': ['chleb', 'pączek', 'bułki'], 'quantity': [3,50,100],
         'unit': ['Kg','Kg','Kg'], 'unit_price': [5.0,70.0,120.0]}

comands = {'exit': sys.exit, 'show': get_items, 'help': help_users, 'add': users_add_list, 'shell': shell}


while True:
    input_user = str
    try:
        input_user = input('plase inpud comands')
        comands[input_user]()
    except KeyError:
        help_users()
    else:
        pass
        # comands[input_user]()
    finally:
        if input_user == 'exit':
            print('Bye Bye!')
