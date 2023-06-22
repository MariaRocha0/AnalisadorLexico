import sys
from lexer import Lexer, TToken

def test_lexer(file_path):
    with open(file_path, 'r') as file:
        input_code = file.read()

    lexer = Lexer(input_code)
    token = lexer.le_token()

    while token.type != TToken.FIM:
        print(token)
        token = lexer.le_token()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Pls add file name as arg.")
        sys.exit(1)

    file_path = sys.argv[1]
    test_lexer(file_path)