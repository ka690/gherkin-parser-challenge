from ply.yacc import yacc
from Gherkin.GherkinLexer import GherkinLexer
from Models.ASTNode import ASTNode

# Parser for Gherkin
class GherkinParser:
    def __init__(self, **kwargs):
        self.lexer = GherkinLexer(**kwargs)
        # TODO: remove debug flag
        self.tokens = self.lexer.tokens
        self.parser = yacc(module=self, **kwargs)

    # Parser rules for each grammar rule which is specified in the docstring.

    def p_feature(self, p):
        # p is a sequence that represents rule contents.
        #
        # feature : FEATURE TEXT scenarios
        #   p[0]     : p[1] p[2] p[3]
        '''
        feature : FEATURE TEXT scenarios
        '''
        p[0] = ASTNode(type='FEATURE', value=p[2], children=p[3])

    def p_scenarios_multiple(self, p):
        '''
        scenarios : scenarios scenario
        '''
        p[0] = p[1] + [p[2]]
        
    
    def p_scenarios_single(self, p):
        '''
        scenarios : scenario
        '''
        p[0] = [p[1]]

    def p_scenario(self, p):
        '''
        scenario : SCENARIO TEXT steps
        '''
        p[0] = ASTNode(type='SCENARIO', value=p[2], children=p[3])

    def p_steps_multiple(self, p):
        '''
        steps : steps step
        '''
        p[0] = p[1] + [p[2]]

    def p_steps_single(self, p):
        '''
        steps : step
        '''
        p[0] = [p[1]]

    def p_step(self, p):
        '''
        step : GIVEN TEXT
            | WHEN TEXT
            | THEN TEXT
            | AND TEXT
        '''
        p[0] = ASTNode(type='STEP:'+p[1].upper(), value=p[2])
    
    def p_error(self, p):
        raise Exception(f'Syntax error at {p.value!r} at line: {p.lineno}')
    
    # def parse(self, data):
    #     return self.parser.parse(data)

    # Test it output
    def test(self, data):
        print(self.parser.parse(data))
