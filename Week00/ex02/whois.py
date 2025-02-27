import sys

def whois(num):
    if num == 0:
        print("I'm Zero.")
    elif num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
        
def main():
    if (len(sys.argv) == 2):
        try:
            whois(int(sys.argv[1]))
        except ValueError:
            print("AssertionError: argument is not an integer")
            
if __name__ == "__main__":
    main()