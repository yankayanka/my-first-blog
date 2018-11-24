print('hello, django girls!')
if 1 > 2:
    print('it works!')
else:
    print('it does\'nt work!')
name = 'sonja'
if name == 'sonja':
    print('hey sonja')
elif name == 'ola':
    print('hey ola')
else:
    print('hey you')

def hallo(name):
    if name == 'ola':
        print('hallo ola')
    elif name == 'sonja':
        print('hallo sonja')
    else:
        print('hallo unbekannte')

hallo('ola')

def hallo(name):
    print('hallo' + name + '!')

hallo('rachel')

def summe(a,b):
    print(a+b)


summe(3, 4)

hallo('sonja')
hallo('peter')

girls = ['rachel', 'monica', 'phoebe', 'ola', 'you']


def hallo(name):
    print('hallo' + name + '!')

girls = ['rachel', 'monica', 'phoebe', 'ola', 'du']
for name_entry in girls:
    hallo(name_entry)
    print('nächstes mädchen')


