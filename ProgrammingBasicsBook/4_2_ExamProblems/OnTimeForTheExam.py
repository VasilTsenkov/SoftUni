import math

h_exam = int(input())
m_exam = int(input())
h_came = int(input())
m_came = int(input())

total_m_exam = (h_exam * 60) + m_exam
total_m_came = (h_came * 60) + m_came

if total_m_came < total_m_exam:
    dif = total_m_exam - total_m_came
    m = dif
    if dif >= 60:
        h = dif / 60
        m = dif % 60
        print(f"Early {math.trunc(h)}:{m:02d} hours before the start")
    elif dif <= 30:
        print(f"On time {m} minutes before the start")
    else:
        print(f"Early {m} minutes before the start")
elif total_m_came > total_m_exam:
    dif = total_m_came - total_m_exam
    m = dif
    if dif >= 60:
        h = dif / 60
        m = dif % 60
        print(f"Late {math.trunc(h)}:{m:02d} hours after the start")
    elif dif < 60:
        print(f"Late {m} minutes after the start")
else:
    print("On time")
