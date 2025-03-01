import sys
def filterwords(words, n):
    return [word for word in words if len(word) > n]

if __name__ == '__main__':
    if len(sys.argv) != 3 or not sys.argv[2].isdigit():
        print("ERROR")
    else:
        print(filterwords(sys.argv[1].split(), int(sys.argv[2])))