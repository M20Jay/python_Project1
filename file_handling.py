# f1 =open("file_1.txt","w+")
# print(f1.tell())
# f1.write("Hi welcome")
# print(f1.tell())
# f1.write("This is python course")
# print(f1.tell())
# f1.seek(0)
# print(f1.tell())
# data=f1.read()
# print(data)
# print(f1.tell())
# f1.close()

f1=open("plt.png", 'rb')
f2=open("plt2.jpg", 'wb')
for i in f1:
    f2.write(i)

print(f1.read())
# print(f1.tell())
# f1.seek(0)
# # f1.write("Hello student")
# print(f1.read())
# f1.write("Jenny's lectures")
