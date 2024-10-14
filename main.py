# cek = int(input())
# for i in range(1,cek + 1):
#     if( i % 3 == 0 )and( i % 5 == 0):
#         print('fizzbuz')
#     elif i % 3 == 0:
#         print('fizz')    
#     elif i % 5 == 0:
#         print('buzz')    
#     else:
#         print(i) 

# str = input()
# coba = range(len(str)//2)
# print(coba)           


# Input dari pengguna
# input_str = input("Masukkan string: ")

# # Mengecek apakah string tersebut palindrom
# if input_str == input_str[::-1]:
#     print("String tersebut adalah palindrom")
# else:
#     print("String tersebut bukan palindrom")


faktorial =int(input())
hasil = 1
for i in range(1,faktorial+1):
    hasil*=i
    print('\n', i,hasil)