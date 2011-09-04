import p0xx
import p1xx
import p2xx
import p3xx
import sys

def main():
    quit = False
    print 'Welcome to Euler Solutions. This application and solutions were written by Jared Dickson.\n'
    while quit != True:
        print "Please enter the integer Id to view the description and the solution,\nor type 'q' to quit"
        
        response = raw_input("Project Id: ")
        print '\n'

        if response == 'q':
            quit = True

        elif response.isdigit():
            response = int(response)

            if response > 0 and response < 100:                
                try:
                    method = getattr(p0xx, ('p' + str(response)))
                    method()
                except:
                    print 'No solution available.'

            elif response >= 100 and response < 200:                
                try:
                    method = getattr(p1xx, ('p' + str(response)))
                    method()
                except:
                    print 'No solution available.'

            elif response >= 200 and response < 300:                
                try:
                    method = getattr(p2xx, ('p' + str(response)))
                    method()
                except:
                    print 'No solution available.'

            elif response >= 300 and response < 400:                
                try:
                    method = getattr(p3xx, ('p' + str(response)))
                    method()
                except:
                    print 'No solution available.'

        print '\n'


if __name__ == '__main__':
    main()