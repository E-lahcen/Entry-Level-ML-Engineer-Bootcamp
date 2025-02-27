import sys
def swap(str):
    swaped = str.swapcase()
    return swaped[::-1]

def main():
    print(swap("Hello World!"))
    
if __name__ == "__main__":
    if (len(sys.argv) == 2):
        print(swap(sys.argv[1]))
    elif (len(sys.argv) == 3):
        print(swap(sys.argv[1] + " " + sys.argv[2]))
    else:
        main()