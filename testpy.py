import argparse 

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--num',
        type=int,
        required=True,
        help='unput for the multiplyby9 function'
    )

    args = parser.parse_args()
    return args

def printhello(): 
    print("hell word") 

def multiplyby9(inputV):
    print(9*inputV)

if __name__=="__main__": #flow program

    input_v = parse_input()
    print(f'the input num is {input_v.num}')
    print("we are in the main function")
    multiplyby9(20)
    printhello()