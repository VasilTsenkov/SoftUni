target_height = int(input())

training_height = target_height - 30
successful_jumps = 0
failed_training = False
all_failed_jumps = 0

while target_height >= training_height:
    new_jump = int(input())
    failed_jumps = 0

    while new_jump < training_height:
        failed_jumps += 1
        if failed_jumps == 3:
            failed_training = True

    if failed_training:
        break

    all_failed_jumps += failed_jumps

    if new_jump > training_height:
        successful_jumps += 1
        training_height += 5

all_jumps = all_failed_jumps + successful_jumps

if failed_training:
    print(f"Tihomir failed at {training_height}cm after {all_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {training_height}cm after {all_jumps} jumps.")