from pympler import asizeof

"""with open('rockyou.txt',encoding='ANSI') as fin:
    with open('rockyouUtf8.txt','w',encoding='utf8') as fout:
        fout.write(fin.read())
"""


def find_word(file_name, pattern):
    with open(file_name, "r", encoding="utf-8", errors="ignore") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if pattern in line:
                yield line


data = find_word(file_name="rockyou.txt", pattern=input("Enter the word: "))


def count_print():
    results = list(data)
    file_obj = open("results.txt", "w", encoding="utf-8", errors="ignore")
    file_obj.writelines(results)
    file_obj.close()

    with open("results.txt", "r") as fhttps://github.com/Kaliny4/Project_Python.gitp:
        x = len(fp.readlines())
        print("Total lines:", x)
        print("Size: ", asizeof.asizeof("results.txt"))


count_print()
