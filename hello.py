# print("Hello, World")
# course = "Linear Algebra"
# print (course.upper())
# print (course.lower())
# print (course.title())
# print (course.rstrip())
# print (course.find("geb"))
# print (10 + 3)
# print (10 - 3)
# print (10 * 3)
# print (10 / 3)
# print (10 // 3)
# print (10 ** 3)
# print (10 % 3)
# bool(0)
# bool("")
# print(bool(None))
# print(10 > 15)
# print(10 < 15)
# print(10 >= 15)
# print(10 <= 15)
# print(10 == 15)
# temprature = 12
# if temprature > 30:
#     print("warm weather, Drink Water")
# elif temprature >= 20 and temprature < 30:
#     print("Nice Weather")
# else:
#     print("It's Cold")
# print("Done")
# # message = "Cold Weather" if temprature > 20 else "Ok"
# # print (message.upper())
# # high_income = True
# # good_commision = True
# # student = True
# # prompt = "Eligible" if (high_income or good_commision) and not student else "Not Eligible"
# # print (prompt.upper())

# for i in range(1, 5):
#     print("Sharjeel")

# top = False
# for i in range(3):
#     print("on top")
#     if top:
#         print("Sharjeel", i + 1, (i + 1) * ".")
#         break
# else:
#     print("Unfortunate")

# for x in range(3):
#     for y in range(5):
#         print(f"({x} ,{y})")
        
# for z in "Python":
#     print(z)

# for k in [1,3,5,7,9]:
#     print(k)
    
# x = 0
# while x % 3 != 1:
#     x = int (input("Enter a number:")) 
#     print (x)
    
# # command = ""
# # while command != "Sharjeel":
# #     if command == "Sharjeel":
# #       print ("Goat")
# #     else:
# #         print("OK")
# # command = input("")
# # print(command)
# count = 0
# for i in range(1 , 10):
#     if i % 2 == 0:
#         count += 1
#         print(i)
# print(f"we have {count} even numbers")

def name(first_name, last_name):
    print(f"hi {first_name}  {last_name}")
    print("you are a champ")
    print("kepp shining bright")
    
    
name("Sharjeel", "Ikhlaq")
         

def multix(number, by):
    return number * by

print(multix(4, 6))