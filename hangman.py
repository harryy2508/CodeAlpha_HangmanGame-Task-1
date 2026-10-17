import random

WORDS = {
    "Programming": {
        "python": "A popular programming language named after a comedy show.",
        "javascript": "A programming language commonly used to make web pages interactive.",
        "variable": "A named storage location for a value.",
        "function": "A reusable block of code that performs a specific task.",
        "compiler": "A program that translates source code into machine code or another target form.",
        "algorithm": "A step-by-step procedure for solving a problem.",
        "database": "An organized collection of data.",
        "software": "A collection of programs and instructions for a computer.",
        "debugging": "The process of finding and fixing errors in code.",
        "integer": "A whole number that can be positive, negative, or zero.",
        "boolean": "A data type that represents true or false.",
        "operator": "A symbol that performs an operation on values.",
        "functionality": "The set of operations a program or system can perform.",
        "recursion": "A technique in which a function calls itself.",
        "iteration": "The repeated execution of a set of instructions.",
        "dictionary": "A Python collection that stores key-value pairs.",
        "tuple": "An ordered Python collection that cannot be modified.",
        "list": "An ordered Python collection that can be changed.",
        "string": "A sequence of characters used to represent text.",
        "exception": "An event that interrupts the normal flow of a program.",
        "inheritance": "An OOP feature that lets a class acquire properties of another class.",
        "polymorphism": "An OOP concept that allows one interface to have different implementations.",
        "encapsulation": "An OOP principle that bundles data and related methods together.",
        "abstraction": "The process of hiding implementation details and exposing essentials.",
        "parameter": "A variable listed in a function definition.",
        "argument": "A value supplied when calling a function.",
        "syntax": "The rules that define valid code structure.",
        "expression": "A combination of values and operators that produces a result.",
        "statement": "An instruction executed by a program.",
        "module": "A Python file containing reusable code.",
        "package": "A structure used to organize related Python modules.",
        "framework": "A reusable foundation for building software applications.",
        "library": "A collection of reusable code that programmers can use.",
        "pointer": "A variable that stores a memory address in languages such as C.",
        "array": "A collection of elements stored under one variable name.",
        "linkedlist": "A data structure made of connected nodes.",
        "stack": "A data structure that follows last in, first out.",
        "queue": "A data structure that typically follows first in, first out.",
        "hashtable": "A data structure that maps keys to values using a hash function.",
        "sorting": "The process of arranging data in a particular order.",
        "searching": "The process of locating an item in a collection.",
        "recurrence": "A relation that defines a sequence using earlier terms.",
        "datastructure": "A way of organizing data for efficient use.",
        "pseudocode": "An informal, language-independent description of an algorithm.",
        "flowchart": "A diagram that represents the steps of a process.",
        "repository": "A place where project files and version history are stored.",
        "git": "A version control system used to track changes in files.",
        "deployment": "The process of making software available for use.",
        "testing": "The process of checking whether software behaves as expected.",
        "refactoring": "Improving code structure without changing its external behavior."
    },

    "Technology": {
        "computer": "An electronic machine that processes data.",
        "laptop": "A portable personal computer.",
        "keyboard": "An input device used to type text and commands.",
        "monitor": "A screen that displays visual output from a computer.",
        "smartphone": "A mobile phone with advanced computing features.",
        "internet": "A global network connecting computers and other devices.",
        "bluetooth": "A wireless technology used for short-range communication.",
        "wireless": "A method of communication that does not require physical cables.",
        "hardware": "The physical components of a computer system.",
        "processor": "The component that executes instructions in a computer.",
        "memory": "A component used to store data and instructions.",
        "storage": "A place where digital information is kept.",
        "database": "An organized system for storing and managing information.",
        "network": "A group of connected devices that communicate with each other.",
        "router": "A device that forwards data between computer networks.",
        "server": "A computer or program that provides services to other computers.",
        "firewall": "A security system that filters network traffic.",
        "encryption": "The process of transforming data to protect its contents.",
        "cybersecurity": "The practice of protecting systems and data from digital attacks.",
        "malware": "Software designed to harm, disrupt, or exploit systems.",
        "phishing": "A deceptive attempt to steal sensitive information.",
        "password": "A secret string used to verify access.",
        "biometrics": "Identification based on physical or behavioral characteristics.",
        "robot": "A programmable machine that performs tasks automatically.",
        "automation": "The use of technology to perform tasks with less human intervention.",
        "artificialintelligence": "Technology that enables machines to perform tasks associated with intelligence.",
        "machinelearning": "A field where computers learn patterns from data.",
        "datascience": "The study of extracting insights from data.",
        "analytics": "The process of examining data to discover useful information.",
        "cloudcomputing": "The delivery of computing services over a network.",
        "virtualization": "The creation of virtual versions of computing resources.",
        "blockchain": "A distributed ledger that records transactions in linked blocks.",
        "cryptocurrency": "A digital asset that uses cryptographic techniques.",
        "sensor": "A device that detects changes in its environment.",
        "satellite": "An object placed in orbit around a celestial body.",
        "drone": "An aircraft that operates without an onboard human pilot.",
        "nanotechnology": "The manipulation of matter at an extremely small scale.",
        "microchip": "A small electronic circuit built on a semiconductor material.",
        "semiconductor": "A material whose electrical conductivity can be controlled.",
        "bandwidth": "The capacity of a communication channel to carry data.",
        "broadband": "High-capacity internet access that supports fast data transmission.",
        "firmware": "Software embedded in a hardware device.",
        "operatingsystem": "Software that manages hardware and application resources.",
        "touchscreen": "A display that also detects touch input.",
        "resolution": "The number of pixels used to represent a digital image or display.",
        "rechargeable": "Capable of having its stored electrical energy restored.",
        "geolocation": "The process of determining the geographic position of a device.",
        "telemedicine": "The delivery of healthcare services using communication technology.",
        "wearable": "An electronic device designed to be worn on the body.",
        "innovation": "The introduction of a new idea, method, or technology."
    },

    "Education": {
        "student": "A person who studies at a school, college, or university.",
        "teacher": "A person who helps others learn.",
        "classroom": "A room where teaching and learning take place.",
        "college": "An educational institution offering further or higher education.",
        "university": "An institution that provides higher education and awards degrees.",
        "textbook": "A book designed to teach a particular subject.",
        "notebook": "A book used for writing notes and information.",
        "homework": "Schoolwork assigned to be completed outside class.",
        "assignment": "A task given to a student for completion.",
        "examination": "A formal assessment of knowledge or skills.",
        "assessment": "The process of measuring learning or performance.",
        "curriculum": "The subjects and content included in an educational program.",
        "syllabus": "An outline of topics covered in a course.",
        "scholarship": "Financial assistance awarded to support education.",
        "graduation": "The completion of an educational program.",
        "certificate": "A document confirming that someone has completed a course or qualification.",
        "degree": "An academic qualification awarded by a college or university.",
        "lecture": "An educational talk delivered to a group of learners.",
        "laboratory": "A room equipped for scientific experiments and practical work.",
        "experiment": "A test performed to investigate an idea or scientific question.",
        "research": "A systematic investigation to discover or understand something.",
        "knowledge": "Information and understanding gained through learning or experience.",
        "learning": "The process of gaining knowledge or skills.",
        "teaching": "The process of helping others acquire knowledge and skills.",
        "discipline": "The practice of following rules and maintaining self-control.",
        "attendance": "The act of being present at a class or event.",
        "timetable": "A schedule showing when classes or activities take place.",
        "principal": "The head of a school.",
        "professor": "A senior academic or a university-level teacher.",
        "lecturer": "A person who teaches through lectures, often at a college or university.",
        "semester": "One of the main academic periods in a school year.",
        "workshop": "A session focused on practical learning and skill development.",
        "seminar": "A meeting where a topic is discussed or studied in depth.",
        "presentation": "A structured explanation of information to an audience.",
        "discussion": "An exchange of ideas or opinions about a subject.",
        "literature": "Written works, especially those valued for artistic or intellectual quality.",
        "mathematics": "The study of numbers, quantities, shapes, and patterns.",
        "chemistry": "The science that studies substances and their properties.",
        "physics": "The science that studies matter, energy, and their interactions.",
        "biology": "The scientific study of living organisms.",
        "geography": "The study of Earth's places, environments, and features.",
        "history": "The study of past events and human societies.",
        "grammar": "The rules governing how words and sentences are structured.",
        "vocabulary": "The collection of words known or used by a person or language.",
        "pronunciation": "The way a word or language is spoken.",
        "comprehension": "The ability to understand written or spoken information.",
        "concentration": "The ability to focus attention on a task.",
        "creativity": "The ability to produce original ideas or solutions.",
        "criticalthinking": "The process of evaluating information logically and carefully.",
        "communication": "The process of sharing information, ideas, or feelings."
    }
}
MAX_ATTEMPTS = 6


def display_menu():
    print("\n" + "=" * 40)
    print("          HANGMAN CHALLENGE")
    print("=" * 40)
    print("1. Start New Game")
    print("2. How to Play")
    print("3. Exit")
    print("=" * 40)


def display_instructions():
    print("\nHOW TO PLAY")
    print("-" * 35)
    print("1. A secret word will be selected randomly.")
    print("2. Guess the word one letter at a time.")
    print("3. Each incorrect guess costs one attempt.")
    print("4. You have a maximum of 6 incorrect guesses.")
    print("5. You can use one hint per round.")
    print("6. Repeated guesses do not cost an attempt.")
    print("7. Guess the complete word to win!")
    print("-" * 35)


def choose_category():
    categories = list(WORDS.keys())

    print("\nChoose a category:")

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    while True:
        choice = input("Enter category number (or 0 for random): ").strip()

        if choice == "0":
            return random.choice(categories)

        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]

        print("Invalid choice. Please try again.")


def display_word(word, guessed_letters):
    return " ".join(
        letter.upper() if letter in guessed_letters else "_"
        for letter in word
    )


def play_round():
    category = choose_category()
    word = random.choice(list(WORDS[category].keys()))
    hint = WORDS[category][word]

    guessed_letters = set()
    incorrect_letters = set()
    attempts_left = MAX_ATTEMPTS
    hint_available = True

    print(f"\nCategory: {category}")
    print("Your secret word is ready!")
    print("Type 'hint' to reveal a clue.")
    print("Type 'quit' to end this round.")

    while attempts_left > 0:
        print("\n" + "-" * 40)
        print("Word:", display_word(word, guessed_letters))
        print("Incorrect guesses left:", attempts_left)
        print(
            "Guessed letters:",
            ", ".join(sorted(guessed_letters | incorrect_letters))
            if guessed_letters or incorrect_letters else "None"
        )
        print("Hints available:", "Yes" if hint_available else "No")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word!")
            print("The word was:", word.upper())
            return True, attempts_left * 10

        guess = input("\nEnter a letter: ").strip().lower()

        if guess == "quit":
            print(f"\nRound ended. The word was {word.upper()}.")
            return False, 0

        if guess == "hint":
            if hint_available:
                print("\nHint:", hint)
                hint_available = False
            else:
                print("You have already used your hint.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic letter.")
            continue

        if guess in guessed_letters or guess in incorrect_letters:
            print("You have already guessed that letter.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Correct! The letter is in the word.")
        else:
            incorrect_letters.add(guess)
            attempts_left -= 1
            print("Incorrect! Try another letter.")

    print("\nGAME OVER!")
    print("The correct word was:", word.upper())

    return False, 0


def main():
    total_score = 0
    games_played = 0
    games_won = 0

    print("\nWelcome to the Hangman Challenge!")

    while True:
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            won, score = play_round()

            games_played += 1
            total_score += score

            if won:
                games_won += 1

            print("\nROUND SUMMARY")
            print("-" * 30)
            print("Games played:", games_played)
            print("Games won:", games_won)
            print("Total score:", total_score)

        elif choice == "2":
            display_instructions()

        elif choice == "3":
            print("\nThanks for playing Hangman!")
            print("Final games played:", games_played)
            print("Final games won:", games_won)
            print("Final score:", total_score)
            print("Better luck and see you next time!")
            break

        else:
            print("Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()