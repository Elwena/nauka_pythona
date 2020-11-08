#  # klucz wartosc
# samolot = {'name': 'boeing',
#            'przebieg': 1000.50,
#            'type': 'pasazerki' }
#
# # lista_dostep_po_kluczy = {'PESEL1': 'Wotjek', 'PESEL2': 'Kat'}
#
# print(samolot['name'])
# print(samolot['przebieg'])
# print(samolot['type'])
#
# samolot['silnik'] = 'odrzutowy'
# # co stanie
# # print(samolot['xyz'])
# # print(samolot.get('xyz'))
#
# print("==== petla po kluczu - key ===")
# for klucz in samolot:
#     print("{0}: {1}".format(klucz, samolot[klucz]))
#
# print("=== petla klucz/wartosc - key/value ===")
# for key, value in samolot.items():
#     print("{0} {1}".format(key, value))

###
 # klucz wartosc
zwierze = {'gatunek': 'kot',
           'wielkosc': 50,
           'kolor': 'szary',
           'rasa': 'syberyjski' }

print(zwierze['gatunek'])
print(zwierze['wielkosc'])
print(zwierze['kolor'])
print(zwierze['rasa'])


print("==== petla po kluczu - key ===")
for klucz in zwierze:
    print("{0}: {1}".format(klucz, zwierze[klucz]))

print("=== petla klucz/wartosc - key/value ===")
for key, value in zwierze.items():
    print("{0} {1}".format(key, value))

###
