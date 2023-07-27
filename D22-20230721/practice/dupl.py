dupl_value=[1,2,2,3,4,1,3]
original_value=[]
for i in dupl_value:
    if i not in original_value:
        original_value.append(i)
print("orginal_list is ",original_value)