pages_in_book = int(input())
pages_read_per_hour = int(input())
days_needed = int(input())

hours_needed_for_book = pages_in_book // pages_read_per_hour
hours_needed_every_day = hours_needed_for_book // days_needed

print(hours_needed_every_day)