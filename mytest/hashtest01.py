from hashlib import sha256

x = 5
y = 0  # We don't know what y should be yet...

z = 0
while sha256(f'{z}'.encode()).hexdigest()[-1] != "0" :
    z += 1
#    print("Result %s - %s - %s" % (z, sha256(f'{z}'.encode()).hexdigest(), sha256(f'{z}'.encode()).hexdigest()[-1]) )

print('**************************************')

print("5x21 %s - %s - %s", sha256(f'{5*21}'.encode()), sha256(f'{5*21}'.encode()).hexdigest(), sha256(f'{5*21}'.encode()).hexdigest()[-1])

print('**************************************')

while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1

#print(f'The solution is y = {y}')