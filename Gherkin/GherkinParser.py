from ply.yacc import yacc
from Errors.ParsingError import ParsingError
from Gherkin.GherkinLexer import GherkinLexer

# Parser for Gherkin
class GherkinParser:
    def __init__(self, **kwargs):
        self.lexer = GherkinLexer(**kwargs)
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
        p[0] = {
            "Type" : 'FEATURE', 
            "Value" : p[2].strip(), # Remove whitespace
            "Children" : p[3],
        }

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
        p[0] = {
            "Type" : 'SCENARIO', 
            "Value" : p[2].strip(), # Remove whitespace
            "Children" : p[3],
        }

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
        p[0] = {
            "Type" : 'STEP:'+p[1].upper(), 
            "Value" : p[2].strip(), # Remove whitespace
        }
    
    def p_error(self, p):
        raise ParsingError(f'Syntax error at {p.value!r} at line: {p.lineno}')
    
    def parse(self, data):
        return self.parser.parse(data)

    # Test it output
    def test(self, data):
        print(self.parser.parse(data))
