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

if __name__ == '__main__':
    fin = open("words.txt")
    #print(fin)
    print_abecedarian()