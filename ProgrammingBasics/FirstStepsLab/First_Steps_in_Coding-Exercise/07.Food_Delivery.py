chicken_meal = int(input())
fish_meal = int(input())
vegetarian_meal = int(input())
delivery = 2.50

price_chicken_meal = chicken_meal * 10.35
price_fish_meal = fish_meal * 12.40
price_vegetarian_meal = vegetarian_meal * 8.15
meal_price = (price_chicken_meal
              + price_fish_meal
              + price_vegetarian_meal)
dessert = meal_price * 0.20
total_price = meal_price + dessert + delivery

print(total_price)
