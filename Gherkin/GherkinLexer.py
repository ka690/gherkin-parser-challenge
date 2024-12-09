from ply.lex import lex

# Lexer/Tokenizer for Gherkin
class GherkinLexer:
    def __init__(self, **kwargs):
        # Build the lexer object using ply.lex
        # TODO: remove debug flag
        self.lexer = lex(module=self, **kwargs)

    # All tokens
    tokens = (
        'FEATURE',
        'SCENARIO',
        'GIVEN',
        'WHEN',
        'THEN',
        'AND',
        'TEXT',
        # 'COMMENT',
    )

    # Ignored characters
    t_ignore = ' \t'

    # Token regex matching rules
    t_FEATURE = r'Feature:'
    t_SCENARIO = r'Scenario:'
    t_GIVEN = r'Given'
    t_WHEN = r'When'
    # t_THEN = r'Then'
    t_AND = r'And'
    t_TEXT = r'.+'
    # TODO: remove if not needed
    # t_COMMENT = r'#'
    t_ignore_COMMENT = r'\#.*'
    
    
    # Define a rule so we can track line numbers
    def t_THEN(self, t):
        r'Then'
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Error handler for illegal characters
    def t_error(self, t):
        print(f'Illegal character {t.value[0]!r} at line {t.lexer.lineno}')
        raise Exception(f'Illegal character {t.value[0]!r} at line {t.lexer.lineno}')
        t.lexer.skip(1)

    # # Build the lexer
    # def build(self,**kwargs):
    #     self.lexer = lex(module=self, **kwargs)

    # Test it output
    def test(self, data):
        self.lexer.input(data)
        while True:
            token = self.lexer.token()
            if not token: 
                break
            print(token)

    # def input(self, data):
    #     self.lexer.input(data)

    # def token(self):
    #     return self.lexer.token()
