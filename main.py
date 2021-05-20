from typing import Mapping
from backward import Backward


"""
    Given the kowledge base:
        
        If X croaks and X eats flies – Then X is a frog
        If X chirps and X sings – Then X is a canary
        If X is a frog – Then X is green
        If X is a canary – Then X is yellow

    And initial facts:

        Fritz croaks
        Fritz eats flies

    Our goal is to decide wether Fritz is green.
"""


if __name__ == "__main__":
    
    ctx = Backward()

    # Defining our knowledge base

    ctx.evaluate("croaks & eatsFlies => frog")
    ctx.evaluate("chirps & sings => canary")
    ctx.evaluate("frog => green")
    ctx.evaluate("canary => yellow")
    
    # Initial facts

    # ctx.evaluate("= croaks eatsFlies")

    # Let's bind some questions to ask the user whenever the value of the variable is unknown.

    ctx.bind_question("croaks", "Does it croak?")
    ctx.bind_question("eatsFlies", "Does it eat flies?")
    ctx.bind_question("chirps", "Does it chirp?")
    ctx.bind_question("sings", "Does it sing?")

    # Ask a question:

    # Is fritz green ?

    answer = ctx.evaluate("green")

    answer = "Yes, Fritz is green." if answer[0] else "No, Fritz is not green."

    print(answer)

    # Is fritz yellow ?

    answer = ctx.evaluate("yellow")

    answer = "Yes, Fritz is yellow." if answer[0] else "No, Fritz is not yellow."

    print(answer)