
list_dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2','color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sorted_list = sorted(list_dict,key=lambda x:x['color'])
print(sorted_list)