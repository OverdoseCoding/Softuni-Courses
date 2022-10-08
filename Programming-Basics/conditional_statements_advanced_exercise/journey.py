budget = float(input())
season = str(input())
place = ''
country = ''

if budget <= 100:
    country = 'Bulgaria'

    if season == 'summer':
        budget *= 0.3
        place = 'Camp'

    elif season == 'winter':
        budget *= 0.7
        place = 'Hotel'

elif budget <= 1000:
    country = 'Balkans'

    if season == 'summer':
        budget *= 0.4
        place = 'Camp'

    elif season == 'winter':
        budget *= 0.8
        place = 'Hotel'

elif budget > 1000:
    country = 'Europe'
    place = 'Hotel'
    budget *= 0.9

print(f"Somewhere in {country}")
print(f"{place} - {budget:.2f}")