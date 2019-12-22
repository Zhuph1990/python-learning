gl_num_list = [6, 3, 9]

# 默认就是升序排序，因为这种应用需求更多
gl_num_list.sort()
print(gl_num_list)

# 只有当需要降序排序时，才需要传递 reverse 参数
gl_num_list.sort(reverse=True)
print(gl_num_list)