import argparse 

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--num',
        type=int,
        required=True,
        help='input for the multiplyby9 function'
    )

    parser.add_argument(
        '--XX',
        type=int,
        default=7,
        help='input for the multiplyby9 function'
    )

    args = parser.parse_args()
    return args

def printhello(): 
    print("hell word") 

def multiplyby9(inputV):
    print(9*inputV)

if __name__=="__main__": #flow program

    input_V = parse_input()
    print(f'the input xx is {input_V.XX}')
    print("we are in the main function")
    multiplyby9(20)
    printhello()