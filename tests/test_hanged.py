from hanged import __version__
from hangman.data_from_faker import faker_color_data,faker_farst_name_data,faker_country_data,faker_word_data,faker_language_data
import random



def test_version():
    assert __version__ == '0.1.0'

def test_faker_type_of_data_1():
    assert type(faker_color_data())==list
    assert type(random.choice(faker_color_data()))==str

def test_faker_type_of_data_2():
    assert type(faker_farst_name_data())==list
    assert type(random.choice(faker_farst_name_data()))==str

def test_faker_type_of_data_3():
    assert type(faker_country_data())==list
    assert type(random.choice(faker_country_data()))==str

def test_faker_type_of_data_4():
    assert type(faker_word_data())==list
    assert type(random.choice(faker_word_data()))==str

def test_faker_type_of_data_5():
    assert type(faker_language_data())==list
    assert type(random.choice(faker_language_data()))==str



