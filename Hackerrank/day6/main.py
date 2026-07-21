# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())


for i in range(T):
    S = input()
    par = ""
    impar = ""
    
    for indice in range(len(S)):
        if indice % 2 == 0:
            par += S[indice]
        else:
            impar += S[indice]
        
    print(par+ " "+ impar)    
