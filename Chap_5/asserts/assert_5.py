# ----------------------------------------FUNCTIONS ------------------------------------
names = {'Esther': 114567, 'Ben': 116745, 'Bob': 456711, 'Dan': 674511}

def phonebook(name):
        if name in names:
            return names[name]
        else:
            return "The name doesn't exist"


sizes = {'A': 4000, 'AA': 2000, 'AAA': 800, 'AAAA': 400}

def battery(size):
    if size not in sizes:
        return "Unknown size"
    power = sizes[size] # base case
    if power >= 4000:
        return "Highest power"
    elif power >= 2000:
        return "High power"
    elif power >= 800:
        return "Medium power"
    else:
        return "Low power"
    
books = {'Chasing reality': 'Bunge, Mario', 'Ruinas Circulares': 'Borges, Jorge Luis', 'Secret Ceremony': 'Denevi, Marco'}

def biblios(book):
    return books[book]

# -------------------------------------------------- TESTS ----------------------------------------------------------
print("Testing phonebook...")
assert phonebook('Esther') == 114567
assert phonebook('Andy') == "The name doesn't exist"

print("Testing battery...")
assert battery('AAA') == "Medium power"
assert battery('AAAAA') == "Unknown size"


print("Testing biblios...")
assert biblios('Ruinas Circulares') == 'Borges, Jorge Luis'

print("✅ All tests passed!")
