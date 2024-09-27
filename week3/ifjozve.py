# ------end will make your sentences stick in one line

print("mahan is the best student ",end="/ ")
print("Ali is good boy")

for i in range(5):   #i=0 , i=1 , i = 2 , i = 3 , 1 = 4    
    print(i,end=" ")  


# ------range(start stop step)

# ------example


    for i in range(2,20,2): #i = 2 4 6 8 10 12 14 16 18
    print(i)


# ------we can use things other than i like j


    for j in range(4,12,5):  #j=9  #(start , end - 1 , step)
    print(j , end = ' ' )


# ------THErE IS A NEW WAY OF SHOWCASING WORLDS PICE BY PIECE

text = "Mahan"

# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3])
# print(text[4])
# print(text)
# character

text = 'amin'

for ch in text:    #ch = "m"
    print(ch,end=" ,") # a,m,i,n


# ------other examples

text = "iran"

for i in text: # i = "i"
    print(i,end="%")


# ------other loops 

for a in range(5): #a = 0
    print(ch)
    print(ch * 2)
    print( 2 * 5 )

# ------list loops

fruits = ["apple", "banana", "cherry"]

for i in fruits: # i = "apple" ,  "banana"
  print(i)

# ------we can also find alphabets in words 

a = "ali"
print('l' in a)

v = "aeiou"
print("m" in v)
print("m" not in v)

# ....

name = "mohammad"
v = "aeiou"

counter = 0
for i in name: #i = "o"
    if i in v:
        counter += 1

# ------ and you can do this

name = input("Enter your name:")
v = input("Enter your v: ")

c = 0  #counter شمارنده
for i in name: # i = 'i'
    if i in  v:
        c += 1
        
print(c)             # 2

# line for =

a = [i*2 for i in range(2)]
a = [i*i  for i in range(2,5)]

# ---- and we can make this shapes 

for i in range(4):  
    for j in range(4): 
        print("-",end=' ')
    print()
    
    """
- - - - 
- - - - 
- - - - 
- - - - 
       
    """


