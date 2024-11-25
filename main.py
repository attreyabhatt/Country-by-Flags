import json
import random
import urllib.request

country_code_file = open("codes.json")
country_code_json = json.load(country_code_file)
country_code_file.close()

country_code_list =  list(country_code_json)
countries_count  = len(country_code_list)

while True:
    random_number = random.randrange(0,countries_count)
    random_country_code = country_code_list[random_number]
    country_name = country_code_json[random_country_code]

    url = "https://flagcdn.com/256x192/" + random_country_code + ".png"

    flag_image = urllib.request.urlretrieve(url,'flag.png')
    # guessed_country = input("Which country does this flag belong to: " + url + "\n")
    guessed_country = input("Which country does this flag belong to: ")
    guessed_country = guessed_country.lower()

    if guessed_country == country_name.lower():
        print("Correct")
    else:
        print("Wrong. The correct answer is: " + country_name + "\n")



