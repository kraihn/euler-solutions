import p0xx
import p1xx
import p2xx
import p3xx
import sys

def main():
    quit = False
    print 'Welcome to Euler Solutions\n'
    while quit != True:
        print "Please enter the integer Id to view the description and the solution,\nor type 'q' to quit"
        response = raw_input("Project Id: ")
        if response == 'q':
            quit = True
        print '\n'


if __name__ == '__main__':
    main()