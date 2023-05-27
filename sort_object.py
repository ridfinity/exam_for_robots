import functools
obj_detected = obj_detected = {'bottle': [110, 30], 'glass': [60, 35], 'book': [310, 23], 'phone': [260, 33], 'dice': [155, 38],
'mouse': [200, 45], 'keyboard': [298, 65], 'fan': [250, 36]}
get_x_axis = functools.partial(lambda x: x[1][0])
sorted_items = sorted(obj_detected.items(), key=get_x_axis, reverse=True)

for item in sorted_items:
    print(item[0], item[1])