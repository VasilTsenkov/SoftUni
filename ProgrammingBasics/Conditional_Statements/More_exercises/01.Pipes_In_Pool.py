pool_volume = int(input())
first_pipe_debit_per_hour = int(input())
second_pipe_debit_per_hour = int(input())
hours_gone = float(input())

first_pipe_volume = first_pipe_debit_per_hour * hours_gone
second_pipe_volume = second_pipe_debit_per_hour * hours_gone
total_volume = first_pipe_volume + second_pipe_volume

if pool_volume >= total_volume:
    pool_percentage_done = (total_volume / pool_volume) * 100
    first_pipe_contribution = (first_pipe_volume / total_volume) * 100
    second_pipe_contribution = 100 - first_pipe_contribution
    print(f"The pool is {pool_percentage_done:.2f}% full. Pipe 1: {first_pipe_contribution:.2f}%. "
          f"Pipe 2: {second_pipe_contribution:.2f}%.")
else:
    pool_overflow = total_volume - pool_volume
    print(f"For {hours_gone:.2f} hours the pool overflows with {pool_overflow:.2f} liters.")
