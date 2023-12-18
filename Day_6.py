
time = 38677673
distance = 234102711571236

start = 0
end = 0

for speed in range(0, time, 1):
    if speed * (time-speed) > distance:
        start = speed
        break

for speed in range(time, 0, -1):
    if speed * (time-speed) > distance:
        end = speed
        break

print(end - start + 1)
