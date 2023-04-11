import os

#print("Текущая директория:", os.getcwd())

# print(os.path.isdir("my_folder"))
# if not os.path.isdir("my_folder"): #проверка на наличие папки в текущей директории
#     os.mkdir("my_folder")

#изменение текущего каталога
os.chdir("new_folder")
# print("Текущая директория:", os.getcwd())
if not os.path.isdir("new2"):
    os.mkdir("new2")
os.chdir("new2")
# print("Текущая директория:", os.getcwd())
# print("Текущая директория:", os.getcwd())
# os.chdir("new_folder/new2")
print("Текущая директория:", os.getcwd())
os.chdir("..")
print("Текущая директория:", os.getcwd())

# os.makedirs("nested1/nested2/nested3") #создание нескольких вложенных папок
