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
textBytes = b"Feature: Guess the word\r\n  Scenario: Maker starts a game\r\n    When the Maker starts a game\r\n    Then the Maker waits for a Breaker to join\r\n\r\n  Scenario: Breaker joins a game\r\n    Given the Maker has started a game with the word silky\r\n    When the Breaker joins the Maker's game\r\n    Then the Breaker must guess a word with 5 characters".decode('utf-8')
textFileContent = 'Feature: Guess the word\r\n\r\n  # The first example has two steps\r\n  Scenario: Maker starts a game\r\n    When the Maker starts a game\r\n    Then the Maker waits for a Breaker to join\r\n\r\n  # The second example has three steps\r\n  Scenario: Breaker joins a game\r\n    Given the Maker has started a game with the word "silky"\r\n    When the Breaker joins the Maker\'s game\r\n    Then the Breaker must guess a word with 5 characters'

lexer = GherkinLexer(debug=False)
lexer.test(textFileContent)

parser = GherkinParser(debug=False)
parser.test(textFileContent)
