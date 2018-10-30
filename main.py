import random

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


startup = startups[random.randint(0, len(startups) - 1)]
industry = industries[random.randint(0, len(industries) - 1)]

print('The ' + startup + ' for ' + industry + '.')
