# Functions of Files:
# 1. write (w) => file_name.write() [write instead of what is written]
# 2. write (a) => file_name.write() [write extra]
# 3. read (r) => print(file_name.read())
# 4. create (x) 

# 5. truncate => file_name.truncate(number of letters)   طباعة عدد الحروف المذكورة فقط وحذف ما بعدها ويسلتزم وجود الملف على وضع append
# f = open(r"C:\Users\Vega Laptop\OneDrive\Documents\eagle\Basel.txt", "a")
# f.truncate(6)

# 6. tell => print(file_name.tell()) 

# 7. seek => file_name.seek(number of letters)   طباعة الحروف المذكورة وحذف ما بعدها 
# f = open(r"C:\Users\Vega Laptop\OneDrive\Documents\eagle\Basel.txt", "r")
# f.seek(10)
# print(f.read())
