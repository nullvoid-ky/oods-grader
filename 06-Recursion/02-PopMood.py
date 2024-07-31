def generate_combinations(num_list, mail_box, answer):
    if mail_box:
        answer.add(int(mail_box))
    if not num_list:
        return
    def loop_index(num_list, mail_box, answer, index):
        if index == len(num_list):
            return
        new_num_list = num_list[:index] + num_list[index+1:]
        generate_combinations(new_num_list, mail_box + num_list[index], answer)
        loop_index(num_list, mail_box, answer, index + 1)
    loop_index(num_list, mail_box, answer, 0)
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
    