if __name__ == '__main__':
    while True:
        try:
            n = int(input())
        except:
            break
        i = 1
        while i % n != 0:
            i = i * 10 + 1
        print(len(str(i)))