# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15 
# 4 8 12 16 20
# 5 10 15 20 25 

print ("no 1")
row = 6
col = 6

for i in range (1 , row):
    for f in range (1 ,col):
        print (f * i, end=" ")
    print ()
    
# 1
# 2 3
# 3 4 5
# 4 5 6 7
# 5 6 7 8 9

print ("no 2")

for i in range (1,6):
    for f in range (i, i+i):
        print (f, end=" ")
    print ()
    
# 1 2 3 4 5 
# 2 3 4 5 
# 3 4 5
# 4 5
# 5

print ("no 3")
n = 5

for i in range(1, n + 1):
    for f in range(i, n + 1):
        print(f, end=" ")
    print()
    
# 1 3 5 7 9
# 2 4 6 8 10 
# 3 5 7 9 11
# 4 6 8 10 12
# 5 7 9 11 13
 
print ("no 4")
row = 5
col = 5

for i in range (1,6):
    num = i
    for f in range (col):
        print(num, end=" ")
        num +=2
    print()
    
# 1 3 5 6 7
# 2 5 8 11 14
# 3 7 11 15 19
# 4 9 13 17 21
# 5 11 15 19 23

print ("no 5")
a = 2

for i in range (1,6):
    b = i 
    for j in range (5):
        print(b, end=" ")
        b += a
    a += 1
    print( )
    
# + + + + 5
# + + + 4 5
# + + 3 4 5
# + 2 3 4 5
# 1 2 3 4 5

print ("no 6")
row = 5
col = 5

for i in range(row, 0, -1):
    for f in range(1, col + 1):
        if f < i:
            print("+", end=" ")
        else:
            print(f, end=" ")
    print()
    
# A B A B A
# B A B A B
# A B A B A
# B A B A B 
 
print ("no 7")
col = 5
row = 4
character = ["A","B"]

for i in range (row):
    for f in range (col):
        print(character[(i + f) % 2], end=" ")
    print()
    
# S O S O S
# O S O S
# S O S
# O S
# S

print ("no 8")
row = 5
character = ["S","O"]

for i in range (row):
    for f in range (row - i):
        print(character[(i + f) % 2], end=" ")
    print( )
    
# Looping jumlah bintang sesuai dengan angka fibonaci

print ("no 9")   
sequence = [0,1]
limit   = 10

while len (sequence) < limit:
    next_num = sequence[-1] + sequence [-2]
    sequence.append(next_num)
    
for num in sequence:
    for _ in range(num):
        print("*", end=" ")
    print()