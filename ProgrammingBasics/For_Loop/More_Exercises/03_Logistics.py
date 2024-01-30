loads_number = int(input())

micro_price = 0
micro_count = 0
truck_price = 0
truck_count = 0
train_price = 0
train_count = 0
total_cargo = 0

for _ in range(loads_number):
    cargo = int(input())
    total_cargo += cargo

    if cargo <= 3:
        micro_price += (200 * cargo)
        micro_count += cargo
    elif cargo <= 11:
        truck_price += (175 * cargo)
        truck_count += cargo
    else:
        train_price += (120 * cargo)
        train_count += cargo

average_price = (micro_price + truck_price + train_price) / total_cargo
micro_percentage = micro_count / total_cargo
truck_percentage = truck_count / total_cargo
train_percentage = train_count / total_cargo

print(f"{average_price:.2f}")
print(f"{micro_percentage:.2%}")
print(f"{truck_percentage:.2%}")
print(f"{train_percentage:.2%}")
