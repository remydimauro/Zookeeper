# put your python code here
hours1 = abs(int(input()))
minutes1 = abs(int(input()))
seconds1 = abs(int(input()))
hours2 = abs(int(input()))
minutes2 = abs(int(input()))
seconds2 = abs(int(input()))
first_event_seconds = ((hours1 * 3600) + (minutes1 * 60) + seconds1)
second_event_seconds = ((hours2 * 3600) + (minutes2 * 60) + seconds2)
print(abs(first_event_seconds - second_event_seconds))
