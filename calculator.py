import argparse

class Calculator:
    def multipy(self, a, b):
        """
        Purpose: multiply 2 values    
        """
        return a * b    
    # end def

if __name__ == '__main__':
    
    calculator = Calculator()
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int, help="first number")
    parser.add_argument("y", type=int, help="second number")
    # parser.add_argument("-v", "--verbosity", action="count", default=0)


    args = parser.parse_args()
    answer = calculator.multipy(args.x, args.y) 
    
    print(f"{args.x} times {args.y} equals {answer}")
