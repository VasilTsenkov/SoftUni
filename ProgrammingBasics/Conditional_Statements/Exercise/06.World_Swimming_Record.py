record_seconds = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

ivan_time = distance_meters * seconds_per_meter
extra_seconds = int((distance_meters / 15)) * 12.5

ivan_total_time = ivan_time + extra_seconds

if ivan_total_time < record_seconds:
    print(f'Yes, he succeeded! The new world record is {ivan_total_time:.2f} seconds.')
else:
    seconds_needed = ivan_total_time - record_seconds
    print(f'No, he failed! He was {seconds_needed:.2f} seconds slower.')
