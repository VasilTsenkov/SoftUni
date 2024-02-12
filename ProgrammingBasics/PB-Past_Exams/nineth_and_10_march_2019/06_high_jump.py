target_jump = int(input())

training_jump = target_jump - 30
failed_attempts = 0
failed_training = False
failed_jumps = 0
successful_jumps = 0
last_jump = 0

while (not failed_training) and target_jump >= training_jump:
    attempt_jump = int(input())

    while attempt_jump <= training_jump:
        failed_attempts += 1

        if failed_attempts == 3:
            failed_training = True
            break

        attempt_jump = int(input())
        continue

    # failed jumps counter
    failed_jumps += failed_attempts

    # resetting the failed attempts counter after a successful jump
    failed_attempts = 0

    # Last jump
    last_jump = training_jump

    # Successful jumps counter
    if attempt_jump > training_jump:
        successful_jumps += 1
        training_jump += 5

# All jumps counter
all_jumps = failed_jumps + successful_jumps

if failed_training:
    print(f"Tihomir failed at {last_jump}cm after {all_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {last_jump}cm after {all_jumps} jumps.")
