# ref: https://youtu.be/Eythq9848Fg

from enum import Enum

class TToken(Enum):
    # caracteres únicos 
    MAIS          = '+'
    MENOS         = '-'
    MUL           = '*'
    DIV           = '/'
    LPAREN        = '('
    RPAREN        = ')'
    LBRACK        = '['
    RBRACK        = ']'
    MAIORQUE      = '>'
    MENORQUE      = '<'
    ATT           = '='
    PONTO         = '.'
    PEV           = ';'
    DOISP         = ':'
    VIRGULA       = ','
    ASPAS         = '"'
    EXCL          = '!'
    QUEST         = '?'
    # comandos condicionais 
    COND            = 'DO, IF, ELSE, THEN'
    # atribuição
    ASSIGNTYPE        = '::, ->, <-'
    # leitura e escrita
    IO            = 'IO, PutStrLn, getLine'
    # misc 
    ID            = 'ID'
    INT_CONST     = 'INT_CONST'
    REAL_CONST    = 'REAL_CONST'
    FIM           = 'FIM' # token que vai indicar que não há mais código para ser analizado (não faz parte do haskell)

class Token:
    # cria o objeto token; __new__ cria e retorna nova instância da classe
    def __new__(cls, type, value, lineno=None, column=None):
        instance = super().__new__(cls)
        instance.type = type
        instance.value = value
        instance.lineno = lineno
        instance.column = column
        return instance

    def __str__(self):
        if self.type in [TToken.COND, TToken.IO]:
            return f"Token = [{self.type.name} {repr(self.value.split(',')[0])}, em: {self.lineno}:{self.column}]"
        elif self.type == TToken.ASSIGNTYPE:
            return f"Token = [{self.type.name} {repr(self.value.split(', ')[0])}, em: {self.lineno}:{self.column})"
        else:
            return f"Token = [{self.type.name} {repr(self.value)}, em: {self.lineno}:{self.column})"

    def __repr__(self):
        return self.__str__()

class Lexer:
    # inicializa o objeto token com os argumentos especificados 
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.lineno = 1
        self.column = 1

    # tratamento de erro
    def handle_error(self):
        if self.current_char is None or not self.current_char.isprintable():
            lexeme = "FIM"
        else:
            lexeme = self.current_char

        error_message = "Caractere não reconhecido '{lexeme}', em: {lineno}:{column}".format(
            lexeme=lexeme,
            lineno=self.lineno,
            column=self.column,
        )
        # print da msg de erro
        print(error_message) 
        # pula o caractere e segue com a análise do resto do código
        self.avanca()

    # função responsável por mover a posição do lexer para o próximo caractere da entrada
    # também guarda a posição de cada um guardando num de linha e coluna
    def avanca(self):
        self.lineno += 1 if self.current_char == '\n' else 0
        self.column = 0 if self.current_char == '\n' else self.column + 1

        self.pos += 1
        self.current_char = None if self.pos > len(self.text) - 1 else self.text[self.pos]

    # função que permite que o lexer avance para o próximo caractere da entrada sem consumi-lo
    # utilizada no token de atribuição para que os caracteres não sejam confundidos com caracteres únicos simples 
    def peek(self):
        peek_pos = self.pos + 1
        return self.text[peek_pos] if peek_pos <= len(self.text) - 1 else None
    
    # função que ignora espaços em branco e quebras de linha
    def ignora_eb_ql(self):
        while self.current_char is not None and self.current_char.isspace():
            self.avanca()

    def numero(self):

        token = Token(type=None, value=None, lineno=self.lineno, column=self.column)

        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.avanca()

        if self.current_char == '.':
            result += self.current_char
            self.avanca()

            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.avanca()

            token.type = TToken.REAL_CONST
            token.value = float(result)
        else:
            token.type = TToken.INT_CONST
            token.value = int(result)

        return token

    def _id(self):

        token = Token(type=None, value=None, lineno=self.lineno, column=self.column)

        value = ''
        while self.current_char is not None and self.current_char.isalnum():
            value += self.current_char
            self.avanca()

        value = value.upper()

        if value in ['DO', 'IF', 'ELSE', 'THEN']:
            token.type = TToken.COND
            token.value = value
        elif value in ['IO', 'PUTSTRLN', 'GETLINE']:
            token.type = TToken.IO
            token.value = value
        else:
            token.type = TToken.ID
            token.value = value
        return token

    def le_token(self):
        # função que "quebra" o código em tokens 

        # ignora espaços em branco e quebras de linha
        while self.current_char is not None:
            if self.current_char.isspace():
                self.ignora_eb_ql()
                continue

            if self.current_char.isalpha():
                return self._id()

            if self.current_char.isdigit():
                return self.numero()

            if self.current_char == ':' and self.peek() == ':':
                token = Token(
                    type=TToken.ASSIGNTYPE,
                    value=TToken.ASSIGNTYPE.value, 
                    lineno=self.lineno,
                    column=self.column,
                )
                self.avanca()
                self.avanca()
                return token
            
            if self.current_char == '-' and self.peek() == '>':
                token = Token(
                    type=TToken.ASSIGNTYPE,
                    value=TToken.ASSIGNTYPE.value,  
                    lineno=self.lineno,
                    column=self.column,
                )
                self.avanca()
                self.avanca()
                return token
            
            if self.current_char == '<' and self.peek() == '-':
                token = Token(
                    type=TToken.ASSIGNTYPE,
                    value=TToken.ASSIGNTYPE.value,  
                    lineno=self.lineno,
                    column=self.column,
                )
                self.avanca()
                self.avanca()
                return token

            # token de caractere único
            try:
                # caso o caractere não exista
                token_type = TToken(self.current_char)
            except ValueError:
                self.handle_error()
            else:
                # cria o token com caractere único e retorna seu próprio valor
                token = Token(
                    type=token_type,
                    value=token_type.value,  
                    lineno=self.lineno,
                    column=self.column,
                )
                self.avanca()
                return token

        # retorna o token que indica que o código acabou
        return Token(type=TToken.FIM, value=None)
