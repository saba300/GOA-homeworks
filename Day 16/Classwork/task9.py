'''9) შემოგდით ორი სია სადაც არის მხოლოდ ინტეჯერები. თქვენი დავალებაა იპოვოთ ამ 
სიაბის წევრების ჯამი და საბოლოოდ დაპრინტოთ ტერმინალში'''

my_list1=[1, 2, 3]
my_list2=[4, 5, 6]
my_list1.extend(my_list2)
sum=0
for i in my_list1:
    sum=sum+i
print(sum)