# emulate switch statements


def if_switch(direction):
    if direction == 'N':
        return "Oh no!  It's a monster!"
    elif direction == 'S':
        return "Oops!  You fell in a hole!"
    if direction == 'E':
        return "Drat...you've been cooked by the sun."
    elif direction == 'W':
        return "Sweet!  You found the damsel in distress ;)"


result = if_switch('W')
print(result)


# example of a switch with lambda calculations
def lambda_switch(fit_request, weight, body_fat):
    # these are not accurate calculations!  Just an example
    return{
        'protein': lambda: weight - (weight * (body_fat / 100)),
        'carbs': lambda: weight - (weight * (body_fat / 100)),
        'fat': lambda: (((weight - (weight * (body_fat / 100))) * 2) * .2),
        'total': lambda: weight + body_fat,
    }.get(fit_request, lambda: None)()


fit_return_protein = lambda_switch('protein', 212, 24.9)
fit_return_carbs = lambda_switch('carbs', 212, 24.9)
fit_return_fat = lambda_switch('fat', 212, 24.9)

protein_calories = fit_return_protein * 4
carb_calories = fit_return_carbs * 4
fat_calories = fit_return_fat * 9
total_calories = protein_calories + carb_calories + fat_calories

print("Your total calorie allowance for each day for week 1 is", total_calories)
