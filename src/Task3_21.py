# dict, {}
cart = {5: [123], 2: [245]}
cart[6] = [64, 21]
print(cart)


def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2*key in d:
        d[2*key] += [value]
    else:
        d[2 * key] = [value]


update_dictionary(cart, 5, "abc")

print(cart)
print(cart[5])