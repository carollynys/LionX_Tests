"""
Analysis of the code below. After your understanding, try to remove the if's clauses without changing their behavior.
"""


def greetings(greeting: str):
    print(greeting)


def say_to(period: str):
    speech: str = ""

    greetings_dict = {"M": "Morning, have a great day!",
                      "A": "Good Afternoon, see you later!",
                      "E": "Good Evening, how was your day?",
                      "N": "Night, sleep well!"}

    speech = greetings_dict.get(g)

    greetings(speech)


if __name__ == "__main__":

    periods = ["M", "A", "E", "M"]
    for g in periods:
        say_to(g)
