delivery_weight = float(input())
type_service = input()
distance_in_km = int(input())
total_price = 0

if type_service == "standard":
    if delivery_weight < 1:
        total_price = distance_in_km * 0.03

    elif delivery_weight >= 1 and delivery_weight < 10:
        total_price = distance_in_km * 0.05

    elif delivery_weight >= 10 and delivery_weight < 40:
        total_price = distance_in_km * 0.10

    elif delivery_weight >= 40 and delivery_weight < 90:
        total_price = distance_in_km * 0.15

    elif delivery_weight >= 90 and delivery_weight < 150:
        total_price = distance_in_km * 0.20

if type_service == "express":
    if delivery_weight < 1:
        total_price = distance_in_km * 0.03
        overprice_for_kg = 0.80 * 0.03
        overprice_for_km = delivery_weight * overprice_for_kg
        total_overprice = distance_in_km * overprice_for_km
        total_price += total_overprice

    elif delivery_weight >= 1 and delivery_weight < 10:
        total_price = distance_in_km * 0.05
        overprice_for_kg = 0.40 * 0.05
        overprice_for_km = delivery_weight * overprice_for_kg
        total_overprice = distance_in_km * overprice_for_km
        total_price += total_overprice

    elif delivery_weight >= 10 and delivery_weight < 40:
        total_price = distance_in_km * 0.10
        overprice_for_kg = 0.05 * 0.10
        overprice_for_km = delivery_weight * overprice_for_kg
        total_overprice = distance_in_km * overprice_for_km
        total_price += total_overprice

    elif delivery_weight >= 40 and delivery_weight < 90:
        total_price = distance_in_km * 0.15
        overprice_for_kg = 0.02 * 0.15
        overprice_for_km = delivery_weight * overprice_for_kg
        total_overprice = distance_in_km * overprice_for_km
        total_price += total_overprice

    elif delivery_weight >= 90 and delivery_weight < 150:
        total_price = distance_in_km * 0.20
        overprice_for_kg = 0.01 * 0.20
        overprice_for_km = delivery_weight * overprice_for_kg
        total_overprice = distance_in_km * overprice_for_km
        total_price += total_overprice

print(f"The delivery of your shipment with weight of {delivery_weight:.3f} kg. would cost {total_price:.2f} lv.")