def locate_group(groups, value):
    for grp in groups:
        if value in grp:
            return grp
    return None

def combine_groups(groups, group_1, group_2):
    merged_group = list(set(group_1 + group_2))
    groups.remove(group_1)
    groups.remove(group_2)
    groups.append(merged_group)

def custom_greedy(groups_data, task_list):
    str1=""

    for task in task_list:
        friend_a, friend_b = task
        group_a = locate_group(groups_data, friend_a)
        group_b = locate_group(groups_data, friend_b)


        if group_a == group_b:
            groups_data.remove(group_a)
            groups_data.append(list(set(group_a + group_b)))
        else:
            combine_groups(groups_data, group_a, group_b)
        str1+=f"{len(groups_data[-1])}\n"
    return str1


with open('input3_1.txt', 'r') as input_data_file:
    num_friends, num_tasks = map(int, input_data_file.readline().split())
    friend_groups = [[i] for i in range(num_friends)]
    task_list = []
    for _ in range(num_tasks):
        start, end = map(int, input_data_file.readline().split())
        task_list.append((start, end))

ans=custom_greedy(friend_groups, task_list)
output_file=open('output3_1.txt','w')
output_file.write(ans)
output_file.close()
