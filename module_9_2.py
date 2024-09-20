first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

print([len(a) for a in first_strings if len(a) >= 5])

print([(a, b) for a in first_strings for b in second_strings if len(a) == len(b)])

print({ab: len(ab) for ab in first_strings + second_strings if len(ab) % 2 == 0})
