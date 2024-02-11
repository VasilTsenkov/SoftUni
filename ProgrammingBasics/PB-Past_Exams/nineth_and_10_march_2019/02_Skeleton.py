quote_minutes = int(input())
quote_seconds = int(input())
length = float(input())
seconds_per_100_meters = int(input())

quote_time = quote_seconds + (quote_minutes * 60)
time_loss = (length / 120) * 2.5
attempt_time = ((length / 100) * seconds_per_100_meters) - time_loss

if attempt_time <= quote_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {attempt_time:.3f}.")
else:
    difference = attempt_time - quote_time
    print(f"No, Marin failed! He was {difference:.3f} second slower.")
