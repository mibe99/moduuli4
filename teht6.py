import random
pisteet = int(input('Anna pisteiden määrä: '))
ympyräpisteet = 0
neliöpisteteet = 0

for i in range(pisteet**2):
    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)
    origin_dist = (rand_y**2 + rand_x**2)
    if origin_dist <= 1:
        ympyräpisteet += 1
    neliöpisteteet += 1
    pi = 4*(ympyräpisteet/neliöpisteteet)
print(f'Arvio piistä: {pi:.10f}')