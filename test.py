from Gherkin.GherkinLexer import GherkinLexer
from Gherkin.GherkinParser import GherkinParser

text = '''
Feature: Guess the word
  Scenario: Maker starts a game
    When the Maker starts a game
    Then the Maker waits for a Breaker to join

  Scenario: Breaker joins a game
    Given the Maker has started a game with the word silky
    When the Breaker joins the Maker's game
    Then the Breaker must guess a word with 5 characters
'''

lexer = GherkinLexer(debug=False)
lexer.test(text)

parser = GherkinParser(debug=False)
parser.test(text)





# from Gherkin import GherkinParser

# parser = GherkinParser()

# text = '''
# Feature: Guess the word

#   # The first example has two steps
#   Scenario: Maker starts a game
#     When the Maker starts a game
#     Then the Maker waits for a Breaker to join

#   # The second example has three steps
#   Scenario: Breaker joins a game
#     Given the Maker has started a game with the word "silky"
#     When the Breaker joins the Maker's game
#     Then the Breaker must guess a word with 5 characters
# '''

# parser.test(text)
