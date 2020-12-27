# 책에 나온대로 하면 역시나 한글이 되지 않음
# with open('read_test.txt') as file_object:
#     contents = file_object.read()
# 
# print(contents)


# encoding='utf-8'
# with open('read_test.txt', encoding='utf-8') as file_object:
#     contents = file_object.read()
#
# print(contents)

def read(file_path, encoding='utf-8', is_all=True):
    with open(file_path, encoding=encoding) as file_object:
        if is_all:
            return file_object.read()
        else:
            return file_object.readlines()


contents = read('read_test.txt')
print(contents.strip())

contents1 = read('text_files/read_test1.txt')
print(contents1)

contents2 = read('text_files/read_test1.txt', is_all=False)
print(contents2)

for content in contents2:
    print(content.strip())