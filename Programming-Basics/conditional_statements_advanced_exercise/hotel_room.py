month = str(input())
days_for_rest = int(input())
studio = 0
apartament = 0

if month in ['May', 'October']:
    studio += 50
    apartament += 65
    if days_for_rest > 14:
        studio *= 0.70
    elif days_for_rest > 7:
        studio *= 0.95
elif month in ['June', 'September']:
    studio += 75.20
    apartament += 68.70
    if days_for_rest > 14:
        studio *= 0.80
elif month in ['July', 'August']:
    studio += 76
    apartament += 77

if days_for_rest > 14:
    apartament *= 0.90

apartament *= days_for_rest
studio *= days_for_rest

print(f'Apartment: {apartament:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')