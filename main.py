numbers/binary.py:
-----------------
binary = input("what binary: ")
exponent = list(binary)
if exponent[1] == "b" or exponent[1] == "B":
    exponent.pop(1)
    exponent.pop(0)
end = 0
exponent.reverse()
for i in range(len(exponent)):
    if exponent[i] == "1":
       end += (2 ** i) 
print(end)

numbers/main.py:
---------------
a = input("What num: ")

b = input("what binary: ")
binary = bin(int(a))
if b == binary[2:]:
    print("good job!!!")
    print(str(binary[2:]) + " = " + a)

words/main.py:
-------------
def turn_into_list(string):
    list1 = []
    for i in range(len(string)):
        list1.append(string[i])
    return string
    
def num_diff_letters(string):
    num = 0
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    vowels = []
    for item in letters:
        if string.lower().find(item) != -1:
            vowels.append(item)
            num += 1
    return str(num)

def num_vowels(string):
    num = 0
    vowels = []
    letters = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    listed = turn_into_list(string)
    for item in letters:
        for item2 in listed:
            if item == item2:
                num += 1
    return str(num)

def num_upercase(string):
    num = 0
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    listed = turn_into_list(string)
    for item in letters:
        for item2 in listed:
            if item == item2:
                num += 1
    return str(num)

def num_of_most_letter(string1):
    num_letters = []
    num = []
    string2 = turn_into_list(string1)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    i = 0
    for item in letters:
        num_letters.append(str(string2.count(item)) + ":" + item)
        num.append(str(string2.count(item)))
    num.sort()
    for item in num_letters:
        if item[0] == num[len(num) - 1]:
            return item[0]
    
    
def num_longest_word(string):
    num = []
    num2 = []
    my_list = list(string)
    for item in my_list:
        if item == ",":
            my_list.remove(",")
    my_string = ("").join(my_list)
    my_list = my_string.split()
    for item in my_list:
        num.append(len(item))
        num2.append(str(len(item)) + ":" + item)
    num.sort()
    for item in num2:
        anum = item[:2]
        bnum = num[len(num) - 1]
        if anum.find(':') != -1:
            
            my_list = list(anum)
            my_list.remove(':')
            anum = ("").join(my_list)
        bnum = str(bnum)
        if anum == bnum:
            word = item[2:]
            if word.find(':') != -1:
                my_list = list(word)
                my_list.remove(':')
                word = ("").join(my_list)
            return word
a = "The quick brown fox, named Roxanne, jumped over Bruno, a lazy dog."
print(num_diff_letters(a))
print(num_vowels(a))
print(num_upercase(a))
print(num_of_most_letter(a))
print(num_longest_word(a))

words/words.py:
--------------
def get_element(string1):
    num = int(string1[0]) - 1
    string = list(string1[2:])
    element = []
    list_of_2nd_elements = []
    for i in range(len(string)):
        element.append(string[i])
        if element.count(" ") != 0:
            element.remove(" ")
        a = ("").join(element)
        a = a.upper()
        element = list(a)
        element.sort()
        try:
            

            list_of_2nd_elements.append(element[num])
        except:
            a = 0
        end = 0
        done = [" "]
        for item in list_of_2nd_elements:
            if list_of_2nd_elements.count(item) != 0 and done.count(item) == 0:
                done.append(item)
                end += 1
    print(end)
get_element("2 Computer")
get_element("2 COMPUTER bat")
get_element("3 COMPUTER")
get_element("4 ACSL is fun")
get_element("9 the xylophone")
get_element("3 python")
get_element("3 computers")
get_element("7 the quick brown fox")
get_element("9 she sells sea shells by the sea shore")
get_element("5 american computer science league")

dan.py:
------
lockers = []


def students(x):
    for i in range(100):
        if x % (i + 1) == 0:
            lockers[x - 1] = flip(lockers[x - 1])
print(lockers)

def flip(x):
    if x == False:
        return True
    else:
        return False
    
for i in range(100):
    lockers.append(False)
for i in range(100):
    students(i + 1)
print(lockers.count(True))

