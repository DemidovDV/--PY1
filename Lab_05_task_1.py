
import pprint

def make_dict(n):
    return [
        {
        'bin' : bin(x),
        'dec' : x,
        'hex' : hex(x),
        'oct' : oct(x)
    } for x in range (n)
    ]

pprint.pprint(make_dict(16))