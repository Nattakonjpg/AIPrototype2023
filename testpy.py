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
    print("Hello word!") 

def multiplyby9(input_V):
    print(9*input_V)

if __name__=="__main__": #flow program

    input_V = parse_input()
    print(f'the input xx is {input_V.XX}')
    print("we are in the main function")
    print(f'the input num is {input_V.num}')
    multiplyby9(input_V.num)
    printhello()