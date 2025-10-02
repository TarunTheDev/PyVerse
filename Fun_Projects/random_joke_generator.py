"""
random_joke_generator.py

Generates a random programming joke.
Uses the 'pyjokes' library if available, otherwise falls back to built-in jokes.
"""

import random

try:
    import pyjokes
    USE_PYJOKES = True
except ImportError:
    USE_PYJOKES = False

# Fallback jokes if pyjokes is not installed
FALLBACK_JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "A SQL query walks into a bar, approaches two tables and asks: 'May I join you?'",
    "How many programmers does it take to change a light bulb? None, it's a hardware problem.",
    "There are 10 types of people in the world: those who understand binary and those who don't.",
    "What's a programmer's favorite hangout place? Foo Bar."
]

def get_random_joke() -> str:
    """Return a random programming joke."""
    if USE_PYJOKES:
        return pyjokes.get_joke()
    return random.choice(FALLBACK_JOKES)


if __name__ == "__main__":
    print("Here’s a programming joke for you:")
    print(get_random_joke())
