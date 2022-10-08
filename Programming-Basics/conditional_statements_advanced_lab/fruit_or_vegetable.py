product_name = input()

fruit = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetable = ['tomato', 'cucumber', 'pepper', 'carrot']

if product_name in fruit:
    print("fruit")
elif product_name in vegetable:
    print("vegetable")
else:
    print("unknown")