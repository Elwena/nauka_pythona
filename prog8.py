samochody = ['syrena', 'polonez']
# lotto = [59, 89, 2, 3, 4]

print(samochody[0])
print(samochody[1])
 #print (samochody[2])

print("===petla 1===")
for s in samochody:
    print(s)

for idx in [0,1]:
    print(samochody[idx])

print("== petla2 po indexie ===")
for idx in range( len(samochody) ):
    print(samochody[idx])
