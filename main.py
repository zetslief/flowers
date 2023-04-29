import csv
from pathlib import Path
import random

def read_adjectives():
    with open('english-adjectives.txt') as f:
        adjectives = f.read().split('\n')
        return adjectives

def read_images():
    folder = Path('flower_photos')
    for flower in folder.glob('*/*.jpg'):
        yield (flower.parent.name, flower)

def shuffle_adjective(name, adjectives):
    return f"{random.choice(adjectives)} {name[:-1]}"

images = [image for image in read_images()]
adjectives = read_adjectives()

for (flower, image) in images:
    print(shuffle_adjective(flower, adjectives))

with open('flower_data.csv', 'w', newline = '') as csvfile:
writer = csv.writer(csvfile)
for (flower, image) in images:
        shuffled_name = shuffle_adjective(flower, adjectives)
        writer.writerow([shuffled_name, str(image)])
