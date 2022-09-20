def palin_string():
    str1 = input("Enter any word : ")
    str_len = len(str1)
    count = 0

    for i in range(0, str_len//2):
        if (str1[i] != str1[str_len - i - 1]):
            count += 1
        else:
            return 0


print(palin_string())