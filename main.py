import random

# List of words to choose from
words = ["apple", "swift", "banana", "hangman", "laptop", "clay", "cake", 
        "pizza", "lactose", "bread", "beach", "water", "sushi", "milkshake", 
        "work", "storm", "bird", "dream", "code", "book", "music", "sun", "moon", 
        "star", "tree", "flower", "ocean", "sky", "cloud", "rain", "snow", "ice", 
        "fire", "earth", "wind", "sand", "rock", "mountain", "river", "lake", 
        "forest", "desert", "field", "meadow", "garden", "house", "home", "street", 
        "road", "car", "bike", "bus", "train", "plane", "ship", "boat", "bridge", 
        "tunnel", "city", "town", "village", "country", "continent", "planet", 
        "universe", "galaxy", "starship", "rocket", "astronaut", "alien", "robot", 
        "computer", "internet", "network", "website", "social", "media", "friend", 
        "family", "parent", "child", "sibling", "cousin", "relative", "partner", 
        "spouse", "love","soul", "mind", "body", "spirit", "emotion", 
        "feeling", "thought", "idea", "concept", "theory", "philosophy", "belief", 
        "religion", "science", "art", "literature", "poetry", "prose", "painting", 
        "drawing", "sculpture", "musician", "artist", "writer", "poet", "scientist", 
        "engineer", "doctor", "lawyer", "teacher", "professor", "student", "pupil", 
        "learner", "scholar", "researcher", "explorer", "discoverer", "inventor", 
        "creator", "maker", "builder", "designer", "architect", "chef", "baker", 
        "cook", "farmer", "gardener", "hunter", "gatherer", "fisherman", "crafter", 
        "artisan", "musician", "singer", "dancer", "actor", "performer", "athlete", 
        "player", "gamer", "puzzle", "game", "sport", "exercise", "activity", "hobby", 
        "interest", "passion", "obsession", "addiction", "habit", "routine", "ritual", 
        "tradition", "culture", "custom", "language", "communication", "conversation", 
        "dialogue", "discussion", "debate", "argument", "disagreement", "conflict", 
        "war", "peace", "harmony", "balance", "justice", "equality", "freedom""liberty", 
        "democracy", "republic", "monarchy", "dictatorship", "tyranny", "anarchy", 
        "government", "politics", "policy", "law", "order", "chaos", "control", "power", 
        "authority", "leadership", "management", "administration", "organization", 
        "institution", "corporation", "company", "business", "enterprise", "startup", 
        "market", "industry", "economy", "finance", "money", "currency", "wealth", 
        "riches", "poverty", "debt", "investment", "profit", "loss", "risk", "reward", 
        "benefit", "cost", "price", "value", "quality", "quantity", "size", "scale", 
        "dimension", "measurement", "distance", "time", "space", "speed", "velocity", 
        "acceleration", "force", "energy", "power", "momentum", "gravity", "friction", 
        "pressure", "temperature", "heat", "cold", "light", "sound", "color", "texture", ]

# Hangman stages
hangman_stages = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

def display_hangman(attempts):
    print(hangman_stages[attempts])

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display)

def hangman_game():
    word = random.choice(words)
    guessed_letters = []
    attempts = 0
    max_attempts = len(hangman_stages) - 1

    print("Welcome to Hangman!")

    while attempts < max_attempts:
        display_hangman(attempts)
        display_word(word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if guess in word and guess not in guessed_letters:
            guessed_letters.append(guess)
        elif guess not in word:
            attempts += 1

        if all(letter in guessed_letters for letter in word):
            print("Congratulations, you won!")
            break
    else:
        display_hangman(attempts)
        print(f"Sorry, you lost! The word was: {word}")

# Run the game
hangman_game()
