#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import array


# In[43]:


matA = array([[8.,5.,6.],\
             [4.,5.,2.,],\
             [9.,7.,10.]])
print("Matrik A =")
print(matA)

matB = array([[5.,5.,6.],\
              [4.,5.,2.],\
             [9.,7.,6.]])
print("Matrik B =")
print(matB)

#praktik 1
print("A + B =")
print(matA+matB)

#praktik 2
print("A - B =")
print(matA-matB)


# In[17]:


#praktik 3
from numpy import array, zeros
A = array([[3.,8.,5.],\
          [6.,4.,7.]])
C = array([[9.,5.,3.],\
          [7.,2.,1.]])
n=2
m=3
D = zeros((n,m))
for i in range (0,n):
    for j in range(0,m):
        D[i][j]=A[i][j]+C[i][j]
        print (D)

# output itu adalah logika penjumlahan A dan C secara urut, 
#  dari baris dan kolom satu hingga baris dan kolom terakhir


# In[39]:


#praktik 4
B = array([[1.,3.],\
          [5.,9.],\
          [2.,4.]])
p=2

E = zeros((n,p))
for i in range(0,n):
    for j in range(0,p):
        for k in range(0,m):
            E[i][j]=E[i][j]+A[i][k]*B[k][j]
            print(E)

# outputnya adalah hasil dari perkalian matriks antara dua matriks A dan B, 
#  menghasilkan matriks baru E. perkaliannya ialah perkalian biasa (bukan perkalian matrik), 
#   di mana setiap elemen matriks hasil diperoleh dengan mengalikan elemen-elemen 
#    yang sesuai dari baris di matriks A dengan kolom di matriks B, lalu menjumlahkannya.


# In[41]:


#praktik 5
A1 = array([[3.,8.,5.],\
           [6.,4.,7.]])
x = array([[2.],\
          [3.],\
          [4.]])
E = zeros((n,1))
for i in range(0,n):
    for k in range(0,m):
        E[i][0]=E[i][0]+A1[i][k]*x[k][0]
        print(E)

# outpunya ialah akan dilakukan perkalian antara matriks A1 dengaan vektor kolom x, 
#  menghasilkan vektor hasil E. untuk operasi komputasi nya mirip seperti praktik 4.


# In[47]:


#praktik 6
X = [[20,9],
     [8,5],
     [9,8]]

result = [[0,0,0],
          [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)

# output nya adalah hasil transpose dari matrik X.
#  (menukar baris menjadi kolom dan kolom menjadi baris)


# In[51]:


#praktik 7
a=5
b=6
c=7
y=a*2+b*3+c*4
print(y)

# outputnya hanyalah operasi aritmatika sederhana. (5x2)+(6x3)+(7x4)


# In[57]:


#praktik 8
def rumus(a,b):
    y=25*a+60*b
    return y

rumus(2,3)

# operasi matematikanya seperti praktik 7, namun kali ini hanya memakai function


# In[68]:


#praktik 9
class matematika():
    def rumus1(a,b,c):
        y=a*2+b*3+c*4
        return y

matematika.rumus1(5,6,7)

# sama seperti praktik sebelumnya, namun kali ini menggunakan class


# In[70]:


#praktik 10
class matematika():
    def rumus2(a,b,c):
        x=a*2+b*3+c*4
        y=a*b*c
        return x,y

matematika.rumus2(5,6,7)

# mirip seperti praktik 9


# In[80]:


#praktik 11
class matematika():
    def rumus3(a,b,c):
        x=a*6+b*8+c*8
        print(x)
        return x
    def rumus4(a,b,c):
        x=a*2+b*3+c*4
        y=a*b*c
        print(x,y)
        return x,y

matematika.rumus3(1,1,1)
matematika.rumus4(2,2,2)

# mirip seperti praktik sebelumnya, bedanya ada 2 function/method.
#  (ada sedikit kesalahan logika pemanggilan return di rumus3, return x ditimpa return x,y. jadi output nya tidak muncul)


# In[24]:


#praktik 12
# class rumus3(a,b,c):
#     x=a*6+b*8+c*8
#     return x

# rumus3(1,1,1)

# agak berbeda dengan praktik 9, nilai x tidak bisa dipanggil melalui return hanya bermodal class


# In[1]:


#praktik 13
class matematika():
    def rumus3(a,b,c):
        x=a*6+b*8+c*8
        # print(x)
        return x
    def rumus4(a,b,c):
        x=a*2+b*3+c*4
        y=a*b*c
        # print(x,y)
        return x,y


# In[30]:


#praktik 14

# melalui cmd "cd C:/Users/arman", "jupyter nbconvert --to script matematika1.ipnyb"
# atau melalui UI Jupiter. file, rename/save as, ubah format .ipynb ke .py


# In[46]:


#praktik 15
class matematika():
    def rumus3(a,b,c):
        x=a*6+b*8+c*8
        # print(x)
        return x
    def rumus4(a,b,c):
        x=a*2+b*3+c*4
        y=a*b*c
        # print(x,y)
        return x,y


# In[26]:


import matematika1


# In[59]:


from matematika1 import matematika


# In[ ]:




