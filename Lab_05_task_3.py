from random import sample, shuffle
from string import ascii_lowercase, ascii_uppercase

def get_random_password(n=8):
    x = (n - n // 4) // 2
    z = n - 2 * x

    password = [
        *sample(ascii_uppercase, x),
        *sample(ascii_lowercase, x),
        *sample([*map(str, [*range(10)])], z)
    ]
    shuffle(password)
    return ''.join(password)

for i in range(100):
    print(get_random_password(n=34))
