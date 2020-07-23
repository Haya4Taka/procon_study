stack_down = []
stack_area = []
for i, chart in enumerate(input()):
    if chart == "\\":
        stack_down.append(i)
    if chart == "/" and stack_down:
        down_i = stack_down.pop()
        area = i - down_i
        if stack_area and stack_area[-1][0] > down_i:
            tmp_area = area
            while stack_area and stack_area[-1][0] > down_i:
                tmp_area += stack_area[-1][1]
                stack_area.pop()
            stack_area.append([down_i, tmp_area])
        else:
            stack_area.append([i, area])

count = 0
area_sum = 0
areas = []
for pond in stack_area:
    count += 1
    area = pond[1]
    area_sum += area
    areas.append(str(area))

print(area_sum)
print(f'{count} {" ".join(areas)}')