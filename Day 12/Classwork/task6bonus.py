'''დაწერეთ პროგრამა რომელიც მომხმარებელს შეეკითხება თავის ასაკს სანამ ასაკი არ იქნება
18 წელზე მეტი შეეკითხეთ თავიდან და როცა ასაკი 18 წელზე ნაკლები იქნება დაუწერეთ რომ არ შეუძლიათ პროგრამაში შესვლა'''
age = int(input("Enter your age: "))
while age>18:
    age = int(input("Enter your age: "))
if age<18:
    print("თქვენ არ შეგიძლიათ პროგრამაში შესვლა")