import random
import requests

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response


#Joke = requests.get('https://v2.jokeapi.dev/joke/Any?safe-mode&type=twopart&format=json%27')

Joke_Setup = []
Joke_Deliver = []

#test_api =




for i in range(10):

    test_api = requests.get('https://v2.jokeapi.dev/joke/Any?safe-mode&type=twopart&format=json%27')
    Joke = test_api.json()


    Joke_Setup.append(Joke['setup'])
    Joke_Deliver.append(Joke['delivery'])

random_num = random.randint(0,len(Joke_Setup))






Tell_Joke = Joke_Setup[random_num]
deliver_joke = Joke_Deliver[random_num]







