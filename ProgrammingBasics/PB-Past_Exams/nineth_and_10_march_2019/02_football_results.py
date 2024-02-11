first_match_score = input()
second_match_score = input()
third_match_score = input()

win_counter = 0
loss_counter = 0
draw_counter = 0

if first_match_score[0] > first_match_score[2]:
    win_counter += 1
elif first_match_score[0] < first_match_score[2]:
    loss_counter += 1
else:
    draw_counter += 1

if second_match_score[0] > second_match_score[2]:
    win_counter += 1
elif second_match_score[0] < second_match_score[2]:
    loss_counter += 1
else:
    draw_counter += 1

if third_match_score[0] > third_match_score[2]:
    win_counter += 1
elif third_match_score[0] < third_match_score[2]:
    loss_counter += 1
else:
    draw_counter += 1

print(f"Team won {win_counter} games.")
print(f"Team lost {loss_counter} games.")
print(f"Drawn games: {draw_counter}")
