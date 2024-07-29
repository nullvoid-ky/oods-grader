def generate_combinations(num_list, current, answer):
    if current:
        answer.add(int(current))
    if not num_list:
        return
    def loop_index(num_list, current, answer, index):
        if index == len(num_list):
            return
        new_num_list = num_list[:index] + num_list[index+1:]
        generate_combinations(new_num_list, current + num_list[index], answer)
        loop_index(num_list, current, answer, index + 1)
    loop_index(num_list, current, answer, 0)
try:
    num_list = input("Enter digits : ").split()
    for i in num_list:
        i = int(i)
        if i > 10 or i < 0:
            exit()
        i = str(i)
    answer = set()
    generate_combinations(num_list, '', answer)
    output = sorted(answer)
    print(f"Output : {output}")
except:
    print("Invalid input")