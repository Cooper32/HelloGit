def factor(number):
# 质数大于 1
   if number > 1:
      for i in range(2,number):
         if (number % i) == 0:
            print(number,"不是质数")
            print(i,end='')
            num1 = number//i
            if num1>=2:
               j = 2
               while j <= num1 :
                  if (num1 % j) == 0:
                     print(" *",j,end='')
                     num1 = num1 // j
                     j = 2
                  else:
                     j = j+1
            else:
               print(' *',num1,end='')
            print(" =",number)
            break
      else:
            print(number,"是质数")
# 如果输入的数字小于或等于 1，不是质数
   else:
      print(number,"不是质数")


a=1
while a==1:
   num = int(input("请输入一个数字: "))
   factor(num)
