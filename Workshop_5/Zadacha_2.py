import copy
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон iPhone'
        },
        'body':{
            'h2':'У нас самая низкая цена на iPhone',
            'div':'Купить',
            'p':'Продать'
        }
    }
}

def change_value(struct, key, value):
    if key in struct:
        struct[key] = value
    else:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                change_value(sub_struct,key,value)
    return struct

def display_struct(struct, spaces=1):
    for key, value in struct.items():
        if isinstance(value, dict):
            print(' ' * spaces, key)
            display_struct(value, spaces + 3)
        else:
            print("{}{} : {}".format(' ' * spaces, key, value))

def make_site(name):
    struct_site = copy.deepcopy(site)
    new_title = 'Куплю/продам {} недорого'.format(name)
    struct_site = change_value(struct_site, 'title', new_title)
    new_h2 = 'У нас самая низкая цена на {}'.format(name)
    struct_site = change_value(struct_site, 'h2', new_h2)
    return struct_site

sites = []
sites_count = int(input('Сколько сайтов: '))
for _ in range(sites_count):
    product_name = input('Введите название продукта для нового сайта: ')
    new_site = make_site(product_name)
    sites.append(new_site)
    for i_site in sites:
        display_struct(i_site)
