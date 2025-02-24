def soma(a,b):
    soma = a+b
    return soma

def twoSun(tabela,target):
    for i in range(tabela):
        for temp in range(i+1, tabela):
            if(tabela[i]+ tabela[temp] == target):
                return(i, temp)
