import math
def sphere_volume(radius):
    """Compute the volume of a sphere given its radius."""
    volume = (4/3) * math.pi * radius ** 3
    return volume


radius = float(input("Enter the radius of the sphere: "))
volume = sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} is: {volume:.2f}")
