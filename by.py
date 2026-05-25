# s=input()
# stop= False
# ln=len(s)
# for i in range(ln//2):
#     for j in range(ln-1,-ln//2,-1):
#         if s[i]!=s[j]:
#             print("Not a Palindrome")
#             stop=True
#             break
#     else:
#         print("Yes its Palindrome")
#     if stop:
#         break
# s = input()

# ln = len(s)

# for i in range(ln // 2):

#     if s[i] != s[ln - i - 1]:

#         print("Not a Palindrome")
#         break

# else:
#     print("Yes its Palindrome")

# def fib(n):
#     l=[0,1]
#     a,b=0,1
#     for i in range(1,n):
#         c=a+b
#         l.append(c)
#         a=b
#         b=c
#     return l[-1]
# num=int(input())
# print(fib(num))

# n=int(input())
# bny=''
# while n != 0:
#     rem=n%8
#     bny=str(rem)+bny
#     n=n//8
# print(bny)

# l=[]
# n=input() 
# for i in range(n):
#     a=int(input())
#     l.append(a)
# d={}
# for i in l:
#     if i in d :
#         d[i]+=1
#     else:
#         d[i]=1
# # print(d) 
# v=[]
# for j in d.values():
#     v.append(j)   
# # # print(v)
# # maxx=max(d.values)
# maxx=v[0]
# for num in v:
#     if num>maxx:
#         maxx=num
        
# for k,v in d.items():
#     if v==maxx:
#         print(f"{k}:{v}")

# s=input()
# for i in range(len(s)//2):
#     if s[i] != s[len(s)-i-1]:
#         print("not palindrome")
#         break
# else:
#     print("palindrome")       
    

# class anagram:
#     def __init__(self,str1, str2):
#         self.str1=str1
#         self.str2=str2
#     def find_anagram(self,str1,str2):
#         self.str1=str1
#         self.str2=str2
        
#         if len(self.str1) != len(str2):
#             return "Not an Anagram"
#         else:
#             for i in str1:
#                 if self.str1.count(i) != self.str2.count(i):
#                     return "Not an Anagram"
#                     break
#             else:
#                 return "Anagram"
# a=input()
# b=input()
# A1=anagram(a,b)
# print(A1.find_anagram(a,b))

def fib(n):
    if n == 1 or n==2:
        return n-1
    
    return fib(n-1) + fib (n-2)
a=int(input())
print(fib(a+1))    

    
            
                          
        
        
        
