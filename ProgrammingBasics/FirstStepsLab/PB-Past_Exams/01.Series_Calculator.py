import math

series = input()
seasons = int(input())
episodes = int(input())
time_episode = float(input())

time_with_ads = time_episode * 1.2
final_episode_minutes = seasons * 10

total_watch_time = seasons * episodes * time_with_ads + final_episode_minutes

print(f"Total time needed to watch the {series} series is {math.floor(total_watch_time)} minutes.")
