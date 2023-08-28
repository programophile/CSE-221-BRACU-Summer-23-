def compute_ways(current_step, ways=[1, 1]):
    if len(ways) <= current_step:
        ways.append(ways[-1] + ways[-2])
        compute_ways(current_step, ways)
    return f'{ways[current_step]}'

def input_output(input_file, output_file):
    input_f = open(input_file, "r")
    output_f = open(output_file, "w")
    n = int(input_f.readline())
    result = compute_ways(n)
    output_f.write(f'{result}\n')
    input_f.close()
    output_f.close()

input_output('input2_1.txt', 'output2_1.txt')
input_output('input2_2.txt', 'output2_2.txt')
input_output('input2_3.txt', 'output2_3.txt')
input_output('input2_4.txt', 'output2_4.txt')
