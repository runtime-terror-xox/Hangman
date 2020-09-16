from faker import Faker


fake=Faker('en_US')

"""
function for get list of color words frome 'Faker' that contain 10 words
"""
def faker_color_data():
    list_of_color=[]
    while len(list_of_color)<10:
        while len(list_of_color)<10:
            fake_color_word = fake.color_name()

            if len(fake_color_word)<=7:
                if fake_color_word in list_of_color:
                    continue
                else:
                    list_of_color.append(fake_color_word)
    return list_of_color


"""
function for get list of first_name words frome 'Faker' that contain 10 words
"""
def faker_farst_name_data():
    list_of_name=[]
    while len(list_of_name)<10:
        while len(list_of_name)<10:
            fake_name_word = fake.first_name()

            if len(fake_name_word)<=7:
                if fake_name_word in list_of_name:
                    continue
                else:
                    list_of_name.append(fake_name_word)
    return list_of_name

"""
function for get list of country words frome 'Faker' that contain 10 words
"""
def faker_country_data():
    list_of_citys=[]
    while len(list_of_citys)<10:
        while len(list_of_citys)<10:
            fake_city_word = fake.country()

            if len(fake_city_word)<=7:
                if fake_city_word in list_of_citys:
                    continue
                else:
                    list_of_citys.append(fake_city_word)
    return list_of_citys

"""
function for get list of words frome 'Faker' that contain 10 words
"""
def faker_word_data():
    list_of_word=[]
    while len(list_of_word)<10:
        while len(list_of_word)<10:
            fake_word = fake.word()

            if len(fake_word)<=7:
                if fake_word in list_of_word:
                    continue
                else:
                    list_of_word.append(fake_word)
    return list_of_word

"""
function for get list of month's name frome 'Faker' that contain 10 words
"""
def faker_month_data():
    list_of_month=[]
    while len(list_of_month)<10:
        while len(list_of_month)<10:
            fake_month = fake.month_name()

            if len(fake_month)<=7:
                if fake_month in list_of_month:
                    continue
                else:
                    list_of_month.append(fake_month)
    return list_of_month

"""
function for get list of languages frome 'Faker' that contain 10 words
"""
def faker_language_data():
    list_of_language=[]
    while len(list_of_language)<10:
        while len(list_of_language)<10:
            fake_language = fake.language_name()

            if len(fake_language)<=7:
                if fake_language in list_of_language:
                    continue
                else:
                    list_of_language.append(fake_language)
    return list_of_language

# print(faker_month_data())
# print(faker_color_data())

if __name__=='__main__':
    assert type(faker_color_data())==list
    assert type(faker_farst_name_data())==list
    assert type(faker_country_data())==list
    assert type(faker_word_data())==list
    # assert type(faker_month_data())==list
    assert type(faker_language_data())==list
    print('all tests passed!!!!')


