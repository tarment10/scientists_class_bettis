#!/usr/bin/env python

def plot_location(lat, lon):
    print("plotting {}/{}".format(lat, lon))


plot_location(18.9, 46.2)
print()

pos = [39.5, 123.34]

plot_location(pos[0], pos[1])
print()

plot_location(*pos)
print()

locations = [
    (1.2, 3.4),
    (3.4, 5.6),
    (8.9, 7.2),
]

for loc in locations:
    plot_location(*loc)

print()

def config(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
    print()


config(color='red', state='PA', person='Bob')

config_values = {
    'color': 'green',
    'state': 'NC',
    'person': 'John',
}

config(**config_values)




