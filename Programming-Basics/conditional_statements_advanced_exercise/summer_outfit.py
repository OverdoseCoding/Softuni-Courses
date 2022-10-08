degrees = int(input())
time_of_the_day = str(input())
outfit = 0
shoes = 0

if time_of_the_day == "Morning":
    if 10 <= degrees & degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"

    if 18 < degrees & degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"

    if degrees >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"

if time_of_the_day == "Afternoon":
    if 10 <= degrees & degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"

    if 18 < degrees & degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"

    if degrees >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"

if time_of_the_day == "Evening":
    if 10 <= degrees & degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"

    if 18 < degrees & degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"

    if degrees >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")