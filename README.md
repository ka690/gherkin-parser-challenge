# Coding Challenge

## Problem Definition

Behaviour-driven development is a methodology for software teams that enables executable specifications for software and testing. Along with this, a syntax called Gherkin was developed to give structure and meaning to these specifications. It consists of 6 primary keywords:

- Feature
- Scenario
- Given
- When
- Then
- And

More rules can be seen in the official Gherkin syntax: [Gherkin Reference](https://cucumber.io/docs/gherkin/reference/).
For this task and simplicity, we will focus primarily on the parsing of keywords above. Here is an example that the program will be expected to pass:

```feature
Feature: Guess the word
  Scenario: Maker starts a game
    When the Maker starts a game
    Then the Maker waits for a Breaker to join

  Scenario: Breaker joins a game
    Given the Maker has started a game with the word silky
    When the Breaker joins the Maker's game
    Then the Breaker must guess a word with 5 characters
```

The task is to implement in Python a language parser for the simplified Gherkin syntax above. To do this, you can use regex expressions to match strings or tools such as ply, which includes a lexer and parser for language definitions. You can find examples of how to use ply here: [ply](https://github.com/dabeaz/ply/tree/master) .

One problem you may want to consider is the precedence of some operators and their effect on the generated abstract syntax tree/execution outcome.

```text
Calculation: 2 + 3 * 4

Standard Precedence:                 Reversed Precedence:

       (+)                                  (*)

      /   \                                /   \

     2     (*)                           (+)    4

          /   \                        /   \

         3     4                       2     3
```

To use the program, it is expected to pass a .txt file over an HTTP endpoint, parse the language and return the abstract syntax tree. If there are errors in parsing the file, this should be returned to the user to help them fix the issues. An extension to this is to think about how we can start executing the generated abstract syntax tree into executable requirements.

## Installation

Clone repository:

```bash
git clone TODO
```

Create a virtual environment and install all the dependencies:

```bash
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Running the Flask API

```bash
py .\app.py
# If you want to run in debug mode
py .\app.py --debug 
```
