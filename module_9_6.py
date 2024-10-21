def all_variants(text):
    for lenght in range(1, len(text) + 1):
        for start in range(len(text) - lenght + 1):
            yield text[start:start+lenght]  



a = all_variants('abc')

for i in a:
    print(i)