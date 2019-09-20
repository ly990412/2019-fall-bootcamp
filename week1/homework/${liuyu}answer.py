#1
def fi(m):
    if m==1:
        return 1
    elif m==2:
        return 1
    else :
        return fi(m-1)+fi(m-2)
    
#2
def temp(st):
 return [st[0],st[-1]]
#3
def even(sa):
    sb=[]
    for i in sa:
        if i % 2==0:
            sb.append(i)
    return sb
#4
def leap(year):
    if year % 4==0 and year % 100!=0:
        return 'leap year'
    elif year % 400==0:
        return 'leap year'
    else:
        return 'not leap year'
#5
def reverse(string):
    
    list1=string.split()
    list1=reversed(list1)
    a = ''.join(list1)
    print(a)
#6
def bs(por):
        buy = por[0]
        por.pop(0)
        pre=[0]
        for price in por:
            if price < buy:
                buy =price
                
            else :
                profit = price-buy
                pre.append(profit)
        return max(pre)
#7

def sting(number,nu):
    numb=list(number)
    nm=str(nu)
    if nm in numb:
        return True
    else:
        return False
#8
def pas(password):
    list2=set(password)
    
    list3={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    list4={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    list5={'0','1','2','3','4','5','6','7','8','9'}
    if list2&list3 != set():
        
        if list2&list4 != set():
            if list2&list5 != set():
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
     
    
            

            
           
       
        
            
    
        


