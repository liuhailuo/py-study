# file = open("demo2_GBK.txt",mode="w",encoding="GBK")

# file.write("1234567890")

# file.close()    

# file = open("a.txt",mode="r",encoding="UTF-8")

# # file.write("1234567890")

# for line in file:
#     print(line)

# file.close()

with open("a.txt",mode="r",encoding="UTF-8") as file:
    data = file.read()
print(data)

