from math import cos

n_days = int(input())
degrees_for_litre_rakja = 0
total_degrees_for_litre_rakja = 0
total_litre_rakja = 0

for i in range(0, n_days):
    litre_rakja = float(input())
    degree_rakja = float(input())

    total_litre_rakja += litre_rakja
    degrees_for_litre_rakja = litre_rakja * degree_rakja
    total_degrees_for_litre_rakja += degrees_for_litre_rakja
    average_degree = total_degrees_for_litre_rakja / total_litre_rakja

print(f'Liter: {total_litre_rakja:.2f}')
print(f'Degrees: {average_degree:.2f}')
if average_degree > 42:
    print("Dilution with distilled water!")
elif average_degree >= 38 and average_degree <= 42:
    print("Super!")
else:
    print("Not good, you should baking!")