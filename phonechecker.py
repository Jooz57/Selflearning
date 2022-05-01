# a = input("Enter your sentence: \n")
# result = len(a)
# print ("Result:", result)

# a = "you are handsome"
# print(a[::-1])



# a = 'on skazal "vy kto takie?"'
# for i in range(len(a)):
#     if a[i] == '"':
#         startpoint = i + 1
#         break
# for i in range(startpoint, len(a)):
#     if a[i] == '"':
#         endpoint = i 
#         break
# print(a[startpoint:endpoint])

# a = 'on skazal "vy kto takie?"'
# startpoint = a.find('"') + 1
# endpoint = a.find('"', startpoint)
# print(a[startpoint:endpoint])

# a = "baby dinosaur"
# mylist = a.split()
# print(" ".join(mylist[::-1]))

# a = "janerooz@yandex.ru"
# print(a[:a.find("@")])

a = ["+7(905)-123-45-67", "8 926 567 89 01"]
for i in range(len(a)):
# for number in a:
    a[i] = a[i].replace('(', '').replace('-', '').replace(')', '').replace(' ', '')
    # .replace('8', '+7')
if a[i][0] == '8':
   a[i] = a[i].replace('8', '+7', 1)

print(a)