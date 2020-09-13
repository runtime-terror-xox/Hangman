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



