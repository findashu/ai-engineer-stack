# file = open("example.txt", "w")

# try:
#     file.write("Hello, World!")
# finally:
#     file.close() # always closing the file

#
with open("ex2.txt", "w") as file:
    file.write("Hello, World!")