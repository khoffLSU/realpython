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