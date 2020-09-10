def merge_the_tools(string, k):
    # your code goes here

    str_len = len(string)
    loop = int(str_len / k)
    for i in range(0, loop):
        char_count = [False] * 150
        str_to_print = ''
        for j in range(0, k):
            idx = (i * k) + j
            if(char_count[ord(string[idx])]):
                continue #jloop
            else:
                char_count[ord(string[idx])] = True
                str_to_print += string[idx]
        print(str_to_print)