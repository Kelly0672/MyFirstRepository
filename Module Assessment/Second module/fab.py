num= input("Enter an integer number") 
num= float(num)
i =1

 
while i<21: 
    if num <=1:
        print (num)
        i+=1
        num = num +1   
    else:       
        a = 1.6186**num
        b= (1-1.6186)**num
        c = (a+b)/2.236
        print('Loop',i,round(c))
        i+=1
        num = num +1 
   

 