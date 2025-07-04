from W13_project import generate_random_unmber,is_prime, get_clues
import pytest

def test_generate_random_number():
    start_range = 1
    end_range = 100
    num = generate_random_unmber(start_range, end_range)
    assert start_range <= num <= end_range

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False

def test_get_clues():
    secret_number = "1234"
    guessed_number = "1360"
    A, B = get_clues(guessed_number, secret_number)
    assert A == 1
    assert B == 1

def test_play_guess_game_easy():
    start_range = 1
    end_range = 50



def test_play_guess_game_medium():
    start_range = 1
    end_range = 100



def test_play_guess_game_hard():
    start_range = 1
    end_range = 1000


pytest.main(["-v", "--tb=line", "-rN", __file__])