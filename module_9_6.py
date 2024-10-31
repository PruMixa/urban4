def all_variants(text):
    length = len(text)
    for i in range(length):
        for j in range(i + 1, length + 1):
            yield text[i:j]


if __name__ == "__main__":
    a = all_variants("abc")
    for i in a:
        print(i)