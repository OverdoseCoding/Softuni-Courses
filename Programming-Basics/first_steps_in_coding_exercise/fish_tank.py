length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input())

capacity_aquarium = length_cm * width_cm * height_cm
capacity_liters = capacity_aquarium / 1000
occupied_space = percent * 0.01
need_liters = capacity_liters * (1 - occupied_space)

print(need_liters)