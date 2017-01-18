def find_max_min(input_list):
  if all(val == input_list [0] for val in input_list) == True:
    list_x = []
    list_x.append(len(input_list))
    return list_x
  else:
    max_val = max(input_list)
    min_val = min(input_list)
    output_list = []
    output_list.append(min_val)
    output_list.append(max_val)
    return output_list