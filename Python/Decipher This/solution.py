import re


def decipher_this(string):
    print("Your string is:", string)
    pattern = "[0-9]{1,}"
    string = string.split(" ")
    result = ""
    counter = 0
    for i in string:
        print("Word[{}]POS[{}]: {}".format(counter + 1, counter, i))
        x = re.search(pattern, i)

        if len(re.split(pattern, i)[1]) < 4:
            j_result = chr(int(x.group())) + re.split(pattern, i)[1][::-1]
            print("\t >>>>", j_result)
            result += j_result + " "
            print("\t Result is now [[[{}]]]".format(result))

        else:
            jresult = ""
            j_char = chr(int(x.group()))
            j_first = re.split(pattern, i)[1][0]
            j_middle = re.split(pattern, i)[1][1:-1]
            j_last = re.split(pattern, i)[1][-1]
            print("\t Before Change:", re.split(pattern, i)[1])
            print("\t 0 (first) = {}".format(j_first))
            print("\t (middle) = {}".format(j_middle))
            print("\t -1 (last) = {}".format(j_last))
            print("\t Chr {}".format(j_char))
            j_result = j_char + j_last + j_middle + j_first
            result += j_result + " "
            print("\t Swapped result is {}".format(j_result))
            print("\t Result is now [[[{}]]]".format(result))
        counter += 1

    result = result.strip()
    print(result)
    return result