'''Witnesses and Counterexamples

In the examples you’ve seen so far, the := assignment expression operator 
does essentially the same job as the = assignment operator in your old code. 
You’ve seen how to simplify code, and now you’ll learn about a different type 
of use case that this operator makes possible.'''

'''
witness = an element that satisfies a check and causes any() to return True
counterexample = an element that doesn't satisfy a check and causes all() to return False'''

cities = ["Vancouver", "Oslo", "Berlin", "Krakow", "Graz", "Belgrade"]

# Does ANY city name start with "B"?
a = any(city.startswith("B") for city in cities)

# Does ANY city name have at least 10 characters?
b = any(len(city) >= 10 for city in cities)

# Do ALL city names contain "A" or "L"?
c = all(set(city.lower()) & set("al") for city in cities)

# Do ALL city names start with "B"?
d = all(city.startswith("B") for city in cities)

# console print
print(a,b,c,d, end='\n')
print('+------+'*3)
# --------------------------- #

"""What if you’re also interested in seeing an example or a counterexample of the 
city names? It could be nice to see what’s causing your True or False result:"""

witnesses = [city for city in cities if city.startswith("B")]

if witnesses:
    print(f"{witnesses[0]} starts with B")
else:
    print("No city starts with B")
print('+------+'*3)

# walrus added in any and all statements
if any((witness := city).startswith("B") for city in cities):
    print(f'{witness} starts with B')

if all((counter := city).startswith("B") for city in cities):
    print('All cities start with B')
else: 
    print(f'{counter} does not start with B')

print('+------+'*3)
def starts_with_b(name):
    print(f'Checking {name}: {(result := name.startswith("B"))}')
    return result

a = any(starts_with_b(city) for city in cities)
print(a) # console return

print('+------+'*3)

b = any(len(witness := city.lower()) > 10 for city in cities)

print(b, f'{witness} last city checked')