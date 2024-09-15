from math import asin, cos, radians, sin, sqrt

# Approximate radius of Earth in kilometers
rad = 6371

# Locations of Oslo and Vancouver
ϕ1, λ1 = radians(59.9), radians(10.8)
ϕ2, λ2 = radians(49.3), radians(-123.1)

# Distance between Oslo and Vancouver
d_Oslo_Vanc = 2 * rad * asin(
    sqrt(
    (ϕhav := sin((ϕ2 - ϕ1) / 2) ** 2) 
    + cos(ϕ1) * cos(ϕ2) * sin((λ2 - λ1) / 2) ** 2))
print(d_Oslo_Vanc)
# 7181.7841229421165

print(ϕhav)

"""The advantage of using the walrus operator here is that you calculate the 
value of the full expression and keep track of the value of ϕ_hav at the same time. 
This allows you to confirm that you didn’t introduce any errors while debugging."""
# ---------------------------------------------------------------------------------#
## Lists and Dictionaries
'''Sometimes when setting up these data structures, you end up performing the same 
operation several times. As a first example, calculate some basic descriptive statistics 
of a list of numbers and store them in a dictionary:'''

numbers = [2, 8, 0, 1, 1, 9, 7, 7]

description = {
    "length": len(numbers),
    "sum": sum(numbers),
    "mean": sum(numbers) / len(numbers),
}

print(description)
# {'length': 8, 'sum': 35, 'mean': 4.375}

# Optimized version of the above code
"""Moving the function calls outside the dictionary to allow calculations to only happen
one time is a basic change.  Using the walrus operator inside the dictionary you gain the 
one time call, and maintain key value definition clarity in the dictionarr."""

numbers = [2, 8, 0, 1, 1, 9, 7, 7]

## Example basic optimization
# num_length = len(numbers)
# num_sum = sum(numbers)

description = {
    "length": (num_length := len(numbers)),
    "sum": (num_sum := sum(numbers)),
    "mean": num_sum / num_length,
}

print(description)
# {'length': 8, 'sum': 35, 'mean': 4.375}