import random
import time

startups = [
    'Uber',
    'Facebook',
    'AirBnB',
    'Linkedin',
    'Spotify',
    'Stripe',
    'Tinder',
    'Amazon',
    'Deliveroo',
    'Deepmind',
    'Instagram',
    'Monzo',
    'PayPal',
    'Netflix',
    'Cooperative',
]

industries = [
    'drones',
    'block chain',
    'authors',
    'big data',
    'bin men',
    'the music industry',
    'magazines',
    'fishing',
    'farming',
    'education',
    'retail',
    'bouncers',
    'drummers',
    'festivals',
    'photographers',
    'sex workers',
    'porn',
    'students',
    'hobos',
    'vegans',
    'cars',
    'carnists',
    'chefs',
    'fast fashion',
    'the laundry industry',
    'old people',
    'friends',
    'surgeons',
    'boob jobs',
    'makeup artists',
    'midwives',
    'dissertations',
    'bird watchers',
    'sports teams',
    'plants'
]


def generate_ideas(number_of_ideas):
    random.seed(float(time.time()))

    ideas = []

    while len(ideas) < number_of_ideas:
        startup = startups[random.randint(0, len(startups) - 1)]
        industry = industries[random.randint(0, len(industries) - 1)]

        idea = 'The ' + startup + ' for ' + industry + '.'
        if idea not in ideas:
            ideas.append(idea)

    return ideas


startup_ideas = generate_ideas(10)

for startup_idea in startup_ideas:
    print(startup_idea)
