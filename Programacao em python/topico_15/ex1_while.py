from statistics import mean
notes = list()

while len(notes) < 5:
    notes.append(float(input(f'Insert your {len(notes)+1}° note: ')))

media = mean(notes)

print(f'Your final mean is {media:.2f}')