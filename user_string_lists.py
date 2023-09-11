"""
Purpose: Illustrate string lists

"""

# imports first
import random

from util_datafun_logger import setup_logger

# reusable functions next
logger, logname = setup_logger(__file__)

# list of grades
list_of_grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]

# list of Courses
list_of_courses = ["Aerospace", "Applied Physics", "Biology", "Business Management", "Chemistry", "Civil Engineering",
                   "Computer Science", "Economics", "Electrical Engineering", "Information Technology",
                   "Mechanical Engineering", "Physics"]
# list of Professors
list_of_professors = ["Mark", "Mike", "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]

# list of first names of students
list_of_student_firstnames = ["Annie", "Brad", "Charlette", "Dave", "Elisabeth", "Francis", "Brad", "Annie"]

# list of last names of students
list_of_student_lastnames = ["Corera", "Pitt", "Rosberg", "Smith", "Swann", "Pitt", "Smith", "Swann"]

# list of outcomes
list_of_outcomes = ["Pass", "Fail"]

# list of semesters
list_of_semesters = ["First", "Second", "Third", "Fourth"]


def string_built_in_functions():
    logger.info("==================string list built-in function==================")
    no_of_courses = len(list_of_courses)
    logger.info(f"Number of Courses available: {no_of_courses}")

    set_of_student_lastnames = set(list_of_student_lastnames)
    logger.info(f"Set of Student last Names: {set_of_student_lastnames}")
    list_of_student_fullnames = [f"{x}, {y}" for (x, y) in zip(list_of_student_firstnames, list_of_student_lastnames)]
    logger.info(f"list of Student full names: {list_of_student_fullnames}")


def create_random_sentence():
    """Create a random sentence from our pre-defined lists"""
    logger.info("Calling create_random_sentence()")

    # Create a random sentence
    # e.g. "The angry dog runs quickly."
    sentence = (f"{random.choice(list_of_professors)} teaches {random.choice(list_of_courses)} "
                f"during {random.choice(list_of_semesters)} semester."
                )

    logger.info(f"Random sentence: {sentence}")


def process_text_zen_of_python():
    """Read in text_zen_of_python.txt and process it"""
    logger.info("Calling process_text_zen_of_python()")

    # read in woodchuck to get a list of words
    with open("text_zen_of_python.txt", "r") as fileObject:
        text = fileObject.read()
        list_words = text.split()  # split on whitespace
        unique_words = set(list_words)  # remove duplicates by making a set

        # Get the count and list of words
        word_ct = len(list_words)

        logger.info(f"The list of words is: {list_words}")
        logger.info(f"There are {word_ct} words in the file.")

        # Print the count and list of unique words
        unique_word_ct = len(unique_words)

        logger.info(f"The set of unique words is: {unique_words}")
        logger.info(f"There are {unique_word_ct} unique words in the file.")

        sort_list_words = sorted(list_words)
        logger.info(f"he list of words in sorted order is: {sort_list_words}")


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# call functions and execute code
# use if __name__ == "__main__":

if __name__ == "__main__":
    string_built_in_functions()
    create_random_sentence()
    process_text_zen_of_python()

    show_log()
