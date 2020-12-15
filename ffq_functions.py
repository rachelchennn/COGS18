"""Module contains functions required to run the Fish Fact Quiz."""

import string

class Question:
    """Creates questions with answer choices and corresponding answer.

    Attributes
    ----------
    prompt: str
        Question to be asked, includes answer options.
    answer: str
        Answer to question, single letter for
        mutltiple choice options from a - d.
    """

    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


def correct_ans(user_input, question, postq_list, question_num):
    """Checks if user input is the correct answer to the question.

    Parameters
    ----------
    user_input: str
        User's input to question.
    question: instance of Question class
        Question that is being asked.
    postq_list: list
        Additional statements that are printed after question
        is answered.
    question_num: int
        Current question number - 1 (so if it were Question 1,
        `question_num` == 0), used for indexing.

    Returns
    ---------
    Printed statement including the statement from `postq_list` that
    corresponds to the question asked.
    May raise ValueError if `user_input` is not the correct answer.
    """

    if user_input == question.answer:
        print("\nNice job!\n\n" + postq_list[question_num] + "\n")
        return True
    else:
        # raises ValueError if answer is incorrect to force
        # out of the loop
        raise ValueError


def hints(user_input, hint_list, question_num):
    """Gives user a hint to the question when requested.

    Parameters
    ----------
    user_input: str
        User's input to question.
    hint_list: list
        List of hints corresponding to the question asked.
    question_num: int
        Current question number - 1 (so if it were Question 1,
        `question_num` == 0), used for indexing.

    Returns
    ---------
    Printed hint statement that corresponds to the question
    asked.
    If a hint is not requested, returns False
    """

    if user_input == 'hint':
        # Adding '\n' before and after to create
        # more spacing between lines
        print("\nHint: " + hint_list[question_num] + "\n")
        return True
    else:
        return False


def invalid_response(user_input, question, valid_input):
    """Prompts user to give a valid response if user input is invalid
    and the incorrect answer.

    Parameters
    ----------
    user_input: str
        User's input to question.
    question: instance of Question class
        Question that is being asked.
    valid_input: list
        List of valid inputs (e.g. list of multiple choice options).

    Returns
    ---------
    Printed statement to ask user to reinput a valid reponse.
    If `user_input` is a valid response, returns False.
    """

    if user_input not in valid_input and user_input != question.answer:
        print("\nThat is not a valid option. Please try again.\n")
        return True
    else:
        return False


def incorrect_ans(user_input, question, postq_list, question_num, valid_input):
    """Prints correct answer if user inputs incorrect answer.

    Parameters
    ----------
    user_input: str
        User's input to question.
    question: instance of Question class
        Question that is being asked.
    postq_list: list
        Additional statements that are printed after question
        is answered.
    question_num: int
        Current question number - 1 (so if it were Question 1,
        `question_num` == 0), used for indexing.
    valid_input: list
        List of valid inputs (e.g. list of multiple choice options).

    Returns
    ---------
    Printed statement of the correct answer and the statement
    from `postq_list` that corresponds to the question asked.
    """

    if user_input in valid_input and user_input != question.answer:
        print("\nOops! That's not quite right. The correct answer was "
              + question.answer + ". \n\n" + postq_list[question_num]+ "\n")
        return True
    else:
        return False


def scores(score, question_list):
    """Generates score earned at the end of the quiz and a pun.

    Parameters
    ----------
    score: int
        Number of correct answers.
    question_list: list
        List of questions asked.

    Returns
    -------
    output: str
        Statement with score earned and a pun.
    """

    score_earned = "You got "+ str(score) + " out of "+ str(len(question_list)) + "."

    if score <= 2:
        output = score_earned + " 'Betta' luck next time!"
    elif score >= 3 and score <= 5:
        output = score_earned + " Looks like you have bigger fish to fry!"
    elif score == 6 or score == 7:
        output = score_earned + " Fin-tastic!"
    elif score == 8 or score == 9:
        output = score_earned + " You're 'piranha' roll!"
    elif score == 10:
        output = score_earned + " Perfect score! You're so so-fish-ticated!"

    return output


def remove_punctuation(user_input):
    # Ensures correct answers with additional punctuation
    # are still correct
    """Removes punctuation from user's input.

    Parameters
    ----------
    user_input: str
        User's input to question.

    Returns
    --------
    out_string: str
        User's input without punctuation.

    Code from COGS18 A3
    """

    out_string = ''

    for character in user_input:
        if character not in string.punctuation:
            out_string = out_string + character
    return out_string


def prep_text(user_input):
    # Ensures correct answers with additional punctuation/capitalization
    # are still correct
    """Removes punctuation from user's input and makes input lowercase.

    Parameters
    ----------
    user_input: str
        User's input to question.

    Returns
    --------
    output: str
        User's input without punctuation or capitalization.

    Code from COGS18 A3
    """

    mod_user_input = user_input.lower()
    output = remove_punctuation(mod_user_input)

    return output


def begin_quiz(question_list, hint_list, postq_list):
    """Initiates Fish Fact Quiz.

    Parameters
    ----------
    question_list: list
        List of questions asked.
    hint_list: list
        List of hints that will print a hint corresponding
        to the question asked when requested.
    postq_list: list
        Additional statements that are printed after question
        is answered.

    Returns
    --------
    Questions from the Fish Fact Quiz, hints when requested, prompts
    to enter valid input if user input is not an accepted option,
    additional statements corresponding to question asked when answered,
    a score at the end of the quiz.
    """
    # Welcome statement (only printed at beginning of quiz)
    print("Welcome to the Fish Fact Quiz! You will be presented with " +
          "10 multiple choice\nquestions about different fishes.\nType " +
          "the letter that corresponds to your selected answer.\nIf you need " +
          "a hint, type 'hint'.\nAt the end of the quiz, you will be " +
          "given a score out of 10 points. Have fun!\n")

    score = 0
    question_num = 0
    valid_input = ['a', 'b', 'c', 'd', 'hint']

    for question in question_list:
        print(str(question_num + 1) + ". " + question.prompt + "\n")

        while True:
            user_input = input('Your answer: ')
            # Takes user_input, removes punctuation and capitalization.
            user_input = prep_text(user_input)

            try:
                # Checks if user_input is the correct answer to the question,
                # prints additional facts about corresponding question.
                correct_ans(user_input, question, postq_list, question_num)
                score += 1
                break

            except ValueError:
                # If hint is requested, prints hint corresponding to question
                # being asked.
                if hints(user_input, hint_list, question_num):
                    continue
                # If user_input is not an acceptable input, prompts user
                # to enter an acceptable input
                elif invalid_response(user_input, question, valid_input):
                    continue
                # If input is an acceptable answer but is wrong, prints the correct
                # answer and additional facts about corresponding question.
                elif incorrect_ans(user_input, question, postq_list, question_num, valid_input):
                    break

        question_num += 1

    print(scores(score, question_list))
    