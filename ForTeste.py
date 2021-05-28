
#Somando elementos em uma lista
list = []
for i in range (10):
    list.append(i)

#função
def soma(list):
    n = 0
    for i in list:
        n = i + n
    return n

print (soma(list))
    
