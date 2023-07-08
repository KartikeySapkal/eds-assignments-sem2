print("Hello World")

name= input("Whats Your Name: ").strip().title()
print(f"Hello {name} Sir")
# print("Hello " + name)
# + is concatination operator
# METHOD IS A BUILT IN FUNCTION

first,last=name.split(" ")

print(f"{first} Sir {last}")
