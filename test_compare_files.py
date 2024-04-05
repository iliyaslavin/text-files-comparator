import os
from compare_files import compare_files

# Фікстура для створення тестових файлів
def setup_module(module):
    with open('file1_test.txt', 'w') as file1, open('file2_test.txt', 'w') as file2:
        file1.writelines(['Hello, world!\n', 'This is a test.\n', 'Python is fun.\n', 'Goodbye!\n'])
        file2.writelines(['Hello, world!\n', 'Testing is essential.\n', 'Python is fun.\n', 'See you later!\n'])

# Фікстура для видалення тестових файлів після виконання тестів
def teardown_module(module):
    os.remove('file1_test.txt')
    os.remove('file2_test.txt')
    os.remove('same.txt')
    os.remove('diff.txt')

# Тест, який перевіряє правильність файлу same.txt
def test_same_file():
    compare_files('file1_test.txt', 'file2_test.txt')
    with open('same.txt', 'r') as file:
        lines = file.readlines()
    assert 'Hello, world!\n' in lines
    assert 'Python is fun.\n' in lines
    assert len(lines) == 2

# Тест, який перевіряє правильність файлу diff.txt
def test_diff_file():
    compare_files('file1_test.txt', 'file2_test.txt')
    with open('diff.txt', 'r') as file:
        lines = file.readlines()
    assert 'This is a test.\n' in lines
    assert 'Goodbye!\n' in lines
    assert 'Testing is essential.\n' in lines
    assert 'See you later!\n' in lines
    assert len(lines) == 4
