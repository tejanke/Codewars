def encrypt_this(text):
    print(text)
    result = ""
    for word in text.split(' '):
        if len(word) == 1:
            w = str(ord(word))
            result += w + " "
        if len(word) == 2:
            w = str(ord(word[0])) + word[1]
            result += w + " "
        if len(word) == 3:
            w = str(ord(word[0])) + word[2] + word[1]
            result += w + " "
        if len(word) > 3:
            second = word[-1]
            last = word[1]
            left = 2
            right = len(word) - 1
            mid = word[left:right]
            w = str(ord(word[0])) + second + mid + last
            result += w + " "
    return result.rstrip()
