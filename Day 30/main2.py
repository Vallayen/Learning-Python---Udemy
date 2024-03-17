# # #catching exceptions

# # try:
# #   file = open("afile.txt")
  
# # except FileNotFoundError:
# #   print("something when wrong with the file, lets make it")
# #   file = open("afile.txtx", "w")
# #   file.write("something")
  
  
# # else:
# #   file.write("hooray it worked")

# # finally:
# #   content = file.read()
# #   print(content)
# #   file.close()
# #   raise KeyError("this is an error i make up") #create own error message

# height = float(input("height: "))
# weight = int(input("Weight: "))

# if height > 3:
#   raise ValueError("This height is invalid unless you are a giant lizard")


# bmi = weight/height ** 2
# print(bmi)