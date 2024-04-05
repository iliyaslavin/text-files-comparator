def read_file(file_path):
    with open(file_path, 'r') as file:
        return set(file.readlines())

def compare_files(file1_path, file2_path):
    file1_lines = read_file(file1_path)
    file2_lines = read_file(file2_path)

    same_lines = file1_lines.intersection(file2_lines)
    diff_lines = file1_lines.symmetric_difference(file2_lines)

    with open('same.txt', 'w') as same_file:
        same_file.writelines(same_lines)

    with open('diff.txt', 'w') as diff_file:
        diff_file.writelines(diff_lines)

if __name__ == "__main__":
    compare_files('file1.txt', 'file2.txt')
