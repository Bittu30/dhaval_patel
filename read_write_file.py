def count_num_in_file(file_path, num):
    count = 0
    with open(file_path, "r") as f:
        for lines in f.readlines():
            tokens = line.split(",")
            count += count_num_in_file(tokens, num)
    return count


def count_num_in_tokens(token, num):
    count = 0
    for token in tokens:
        if num == int(token):
            count += 1
        return count


def sum_numbers(file_path):
    output_files = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            token = line.split(",")
            total = sum_tokens(tokens)
            output_lines.append("sum:" + str(total) + "|" + line)
    with open(file_path, "w") as f:
        f.writelines(output_files)


def sum_tokens(tokens):
    sum = 0
    for token in tokens:
        sum += int(token)
    return sum


# sum_numbers("")
