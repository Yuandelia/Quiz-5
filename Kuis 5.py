#PYTHON EXPRESSION

#Menentukan Hasil Ekspresi
print("1. Menentukan Hasil Ekspresi")
print("a.", 15 % 5)  
print("b.", 12 + 3*5 == 75)
print("c.","PML" + "15523")
print("d.","100" + str(234))
print("e.",((11%3) + 2) != 8/2)
print('')

#Ekspresi Boolean
p = 11
q = 5
r = 4
print('2. Ekspresi Boolean')
print("a.", (p-r) == (r+q)) 
print("b.", ((p%3)+q)!=(r%2))  
print("c.", (q-3)==(p%2+q)) 
print("d.",(r+q)!=((p*2)%2))  
print("e.", (((q%3)+p)>(r%2)))
print("f.",((r+p))<=(q*5)) 
print('')

#ISIAN SINGKAT
#1. Hasil dari cuplikan kode
print('ISIAN SINGKAT')
print('1. Hasil dari cuplikan kode')
print("Honey" + "Boo"*3) 
print('')

print('2.Hasil Pemanggilan Fungsi Capitals')
capitals = {}
capitals['Murica'] = 'Warshington'
capitals['Germany'] = 'Bonn'
capitals['France'] = 'Paris'
capitals['Engalnd'] = 'London'
capitals['Germany'] = 'Berlin'
print(capitals['Germany'])
print('')

print('3. Hasil dari Potongan Kode')
a = "23"
b = "9"
print(a + b)
print('')

print('4. Definisi List alam Python')
letters = ["a", "b", "o", "c", "p"]
print("a.", letters[1])
print("b.", letters[len(letters)-2] )
print("c.", letters + ["x"]) 
print("d.", letters)
print('')

print('5. Hasil Kode')
hasil= ' '.join('h a n d s'.split())
print(hasil)
print('')

print('6.Json')
json_string = "deux"
print(json_string)
print('')

print('7. Pembagi Indeks')
def pembagi_indeks1(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
        return -1
    
vals = [101,4,12,24]
print(pembagi_indeks1(vals, 2))
print('')

print('8. Melengkapi Kode dan Melakukan Panggilan ')
def mystery (n,m):
    p = 0
    e = 0
    while p < n :
        p= p + 1
        e = 0
    return p
print(mystery(4,3))