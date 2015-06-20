#print(fin.readline())
#line = fin.readline()
#words = line.strip()

def has_no_e(word):
    """
    :return: True - if the given word doesn't have the letter "e" in it.
    False - otherwise.
    """
    for char in word:
        if char in "Ee":
            return False
    return True


def print_no_e():
    """ print only the words from the list that have no “e”. Computes and prints
    the percentage of the words in the list have no “e.”
    :return: none
    """
    count_no_e = 0
    count_total = 0
    for line in fin:
        word = line.strip()
        if has_no_e(word):
            #print(word)
            count_no_e += 1
        count_total += 1
    percent = (count_no_e/count_total)*100
    print('Words total:', count_total)
    print('Words that have no "e":', count_no_e)
    print('Percentage of words that have no "e":', round(percent, 2))


def avoids(word, avoid_str):
    """
    :param word: a word which will be examined on the presence of forbidden letters.
    :param avoid_str: a string of forbidden letters.
    :return: True - if the word doesn't contain any of the forbidden letters.
    False - otherwise.
    """
    for char in word:
        if char in avoid_str:
            return False
    return True


def print_avoids():
    """ Prompts the user to enter a string of forbidden letters
    and then prints the number of words that don’t contain any of them.
    :return: none
    """
    avoid_str = input('Enter a string of forbidden letters, please:')

    count_avoids = 0
    for line in fin:
        word = line.strip()
        if avoids(word, avoid_str):
            print(word)
            count_avoids += 1
    print('Number of words that don\'t contain any of the forbidden letters:', count_avoids)


def uses_only(word, only_str):
    """
    :param word: a word which will be examined on the presence of the letters.
    :param only_str: a string of letters.
    :return: True - if the word if the word contains only letters in the string.
    False - otherwise.
    """
    for char in word:
        if char not in only_str:
            return False
    return True

def print_uses_only():
    """ Prompts the user to enter a string of letters
    and then prints words that contain only letters in the string. Prints total number of these words.
    :return: none
    """
    str = input('Enter a string of letters, please:')

    count_uses_only = 0
    for line in fin:
        word = line.strip()
        if uses_only(word, str):
            print(word)
            count_uses_only += 1
    print('Number of words that contain only letters in the string:', count_uses_only)


def uses_all(word, all_str):
    """
    :param word: a word which will be examined on the presence of the letters.
    :param all_str: a string of letters.
    :return: True - if the word uses all the letters in the string.
    False - otherwise.
    """
    for char in all_str:
        if char not in word:
            return False
    return True

def print_uses_all():
    """ Prompts the user to enter a string of letters
    and then prints words that use all letters in the string. Prints total number of these words.
    :return: none
    """
    str = input('Enter a string of letters, please:')

    count_uses_all = 0
    for line in fin:
        word = line.strip()
        if uses_all(word, str):
            print(word)
            count_uses_all += 1
    print('Number of words that use all letters in the string:', count_uses_all)


def is_abecedarian(word):
    """
    :param word: a word.
    :return: True - if the letters in the word appear in alphabetical order (double letters are ok).
    False - otherwise.
    """
    prev_letter = word[0]
    for char in word:
        if char < prev_letter:
            return False
        prev_letter = char
    return True


def print_abecedarian():
    """ Prints words which letters are in alphabetical order. Prints total number of these words.
    :return: none
    """
    count_abc = 0
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            print(word)
            count_abc += 1
    print('Number of words which letters are in alphabetical order:', count_abc)


def is_3doubles(word):
    """
    :param word: a word.
    :return: True - if the word has three consecutive double letters.
    False - otherwise.
    """
    count = 0
    flag = 0
    prev_letter = word[0]
    for char in word[1:]:
        #print(char)
        if flag == 0:
            if char == prev_letter:
                count += 1
                flag = 1
                if count == 3:
                    return True
                #print(count)
            else:
                count = 0
        else:
            flag = 0
        prev_letter = char

    return False


def print_3doubles():
    """ Prints words that have three consecutive double letters. Prints total number of these words.
    :return: none
    """
    count_3d = 0
    for line in fin:
        word = line.strip()
        if is_3doubles(word):
            print(word)
            count_3d += 1
    print('Number of words that have three consecutive letters:', count_3d)


def is_palindrome(number, begin, end):
    """
    :param number: any number
    :param begin: what digit to start with
    :param end: what digit to finish with
    :return: True - if the digits between 'end' and 'start' are palindromic; False - otherwise.
    """
    while begin < end:
        if number[begin] != number[end]:
            return False
        begin += 1
        end -= 1
    return True


def print_pals():
    """ examines all 6 digit numbers for the requirements: 1) I noticed that the last 4 digits were palindromic.
        2) One mile later, the last 5 numbers were palindromic.
        3) One mile after that, the middle 4 out of 6 numbers were palindromic.
        4) One mile later, all 6 were palindromic.
        Prints the number that was on the odometer at the step 1).
    :return: none
    """
    i = 100000
    while i < 1000000:
        if is_palindrome(str(i), 2, 5):
            j = i + 1
            if is_palindrome(str(j), 1, 5):
                j += 1
                if is_palindrome(str(j), 1, 4):
                    j += 1
                    if is_palindrome(str(j), 0, 5):
                        print(i)
        i += 1

def is_reverse2d(num1, num2):
    """ The function is created specifically for the purposes of 'print_ages()'.
    :param num1: any number 1- or 2-digit number. If the number consists of 1 digit then the function adds a zero on the left.
    :param num2: any 2-digit number.
    :return: True - if the reverse of 'num1' written as string is equal to 'num2' written as string.
    False - otherwise.
    """
    num1 = str(num1)
    num2 = str(num2)
    num1 = num1.zfill(2)

    return num1[::-1] == num2


def print_ages():
    """ The function goes through all possible ages of a child and his parent and counts how many times their ages are
    reversible (an example of reversible ages: a child is 12, and his parent is 21). Any time the reversible ages are
    found, the child's age is saved in a list. The function prints the list of the child's ages when there are 8 or more
    reversible ages happened over the life.
    :return: none
    """
    for i in range(1, 100):
        count = 0
        lst = []
        my_age = i
        for j in range(i+10, 110):
            her_age = j
            if is_reverse2d(my_age, her_age):
                count += 1
                lst.append(my_age)
                #print(lst)
            if count >= 1:
                my_age += 1
            else:
                my_age = i

        if count >= 8:
            print(lst)



if __name__ == '__main__':
    #fin = open("words.txt")
    #print(fin)
    print_ages()
