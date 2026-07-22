# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
mapa ={}

for i in range(n):
    name, phone = input().strip().split()
    
    mapa[name] = phone
    
while True:
    try:
        buscar = input().strip()
        if buscar in mapa:
            print(f"{buscar}={mapa[buscar]}")
        else:
            print("Not found")
    except EOFError:
        break
