N= int(input('Введите количество чисел: '))
spisok=list(map(int,input().split()))
e=set(spisok)
print(len(e))