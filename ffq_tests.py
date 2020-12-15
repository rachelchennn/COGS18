"""Module containts tests for functions used in the Fish Fact Quiz."""

import ffq_functions as func
import ffq_req_inputs as inp

valid_input = ["a", "b", "c", "d", "hint"]

def test_correct_ans():
    """Tests function `correct_ans()`."""

    assert callable(func.correct_ans)
    assert func.correct_ans("d", inp.Q1, inp.postq_list, 0) is True
    assert func.correct_ans("c", inp.Q5, inp.postq_list, 4) is True


def test_hints():
    """Tests function `hints()`."""
    assert callable(func.hints)
    assert func.hints("hint", inp.hint_list, 3) is True
    assert func.hints("a", inp.hint_list, 3) is not True


def test_invalid_response():
    """Tests function `invalid_response()`."""
    assert callable(func.invalid_response)
    assert func.invalid_response("eee", inp.Q1, valid_input) is True
    assert func.invalid_response("a", inp.Q1, valid_input) is not True


def test_incorrect_ans():
    """Tests function `incorrect_ans()`."""
    assert callable(func.incorrect_ans)
    assert func.incorrect_ans("b", inp.Q5, inp.postq_list, 4, valid_input) is True
    assert func.incorrect_ans("d", inp.Q1, inp.postq_list, 0, valid_input) is not True


def test_scores():
    """Tests function `scores()`."""
    assert callable(func.scores)
    assert "Fin-tastic!" in func.scores(7, inp.question_list)
    assert "'Betta' luck next time!" in func.scores(1, inp.question_list)


def test_prep_text():
    """Tests function `prep_text()`."""
    assert callable(func.prep_text)
    assert func.prep_text("!/?>A\\") == "a"
    assert func.prep_text("!H((*i#N$#t@#s") == "hints"
    