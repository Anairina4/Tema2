#Exercitiul 1 metoda cu if si veificare normala
sum = 0
def your_function(*args, **kwargs):
   for i in args:
      global sum
      if type(i) == int or type(i) == float:
          sum =  sum + i
      else:
         print('Not an int or float')

   return sum

#your_function(1,5,-3,'abc',[12,6,'cad'])
#print(sum)

#your_function()
#print(sum)

your_function(2,4,'abc', param_1=2)
print(sum)


# Exercitiul 1 metoda cu isinstance
sum = 0
def your_function(*args, **kwargs):
   for i in args:
      global sum
      if isinstance(i,int) or isinstance(i,float):
          sum =  sum + i
      else:
         print('Not an int or float')

   return sum

#your_function(1,5,-3,'abc',[12,6,'cad'])
#print(sum)

#your_function()
#print(sum)

your_function(2,4,2,4.7,'abc', param_1=2)
print(sum)


#Exercitiul 1 folosind tratare exceptii
sum = 0
def your_function(*args, **kwargs):
   for i in args:
      global sum

      try:
         sum += i
      except TypeError as e:
         print('Not int or float')

   return sum

your_function(1,5,-3,'abc',[12,6,'cad'])
print(sum)

#your_function()
#print(sum)

#your_function(2,4,2,4.7,'abc', param_1=2)
#print(sum)


#Exercitiul 2
#suma tuturor numerelor
def my_function(n):

   if n==0:
      return 0

   return n + my_function(n-1)

print(my_function(10))


#suma numerelor pare
def my_function(n):

   if n == 0:
      return 0

   if n % 2 == 0:
      return n + my_function(n-1)
   else:
      return my_function(n-1)

print(my_function(10))


#suma numerelor impare
def my_function(n):

   if n==0:
      return 0

   if n % 2 == 1:
      return n + my_function(n-1)
   else:
      return  my_function(n-1)


print(my_function(5))


# Exercitiul 3
def citire_numar():

   my_number = input("My number is:")
   try:
      my_int = int(my_number)
      print(my_int)
   except ValueError as e:
      print("0")

citire_numar()



