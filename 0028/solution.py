"""
The All-Berland National Olympiad in Informatics has just ended! Now Vladimir wants to upload the contest from the Olympiad as a gym to a popular Codehorses website.

Unfortunately, the archive with Olympiad's data is a mess. For example, the files with tests are named arbitrary without any logic.

Vladimir wants to rename the files with tests so that their names are distinct integers starting from 1 without any gaps, namely, "1", "2", ..., "n', where n is the total number of tests.

Some of the files contain tests from statements (examples), while others contain regular tests. It is possible that there are no examples, and it is possible that all tests are examples. Vladimir wants to rename the files so that the examples are the first several tests, all all the next files contain regular tests only.

The only operation Vladimir can perform is the "move" command. Vladimir wants to write a script file, each of the lines in which is "move file_1 file_2", that means that the file "file_1" is to be renamed to "file_2". If there is a file "file_2" at the moment of this line being run, then this file is to be rewritten. After the line "move file_1 file_2" the file "file_1" doesn't exist, but there is a file "file_2" with content equal to the content of "file_1" before the "move" command.

Help Vladimir to write the script file with the minimum possible number of lines so that after this script is run:  all examples are the first several tests having filenames "1", "2", ..., "e", where e is the total number of examples;  all other files contain regular tests with filenames "e + 1", "e + 2", ..., "n", where n is the total number of all tests. 


-----Input-----

The first line contains single integer n (1 ≤ n ≤ 10^5) — the number of files with tests.

n lines follow, each describing a file with test. Each line has a form of "name_i type_i", where "name_i" is the filename, and "type_i" equals "1", if the i-th file contains an example test, and "0" if it contains a regular test. Filenames of each file are strings of digits and small English letters with length from 1 to 6 characters. The filenames are guaranteed to be distinct.


-----Output-----

In the first line print the minimum number of lines in Vladimir's script file.

After that print the script file, each line should be "move file_1 file_2", where "file_1" is an existing at the moment of this line being run filename, and "file_2" — is a string of digits and small English letters with length from 1 to 6.


-----Examples-----
Input
5
01 0
2 1
2extra 0
3 1
99 0

Output
4
move 3 1
move 01 5
move 2extra 4
move 99 3

Input
2
1 0
2 1

Output
3
move 1 3
move 2 1
move 3 2
Input
5
1 0
11 1
111 0
1111 1
11111 0

Output
5
move 1 5
move 11 1
move 1111 2
move 111 4
move 11111 3
"""

def min_script_for_test_files(n: int, files: list) -> tuple:
    """
    Generate a script with minimum number of "move" commands to rename test files.
    
    Args:
        n: Number of files with tests (1 ≤ n ≤ 10^5)
        files: List of n files, where each file is represented by [name, type]
              name: Filename (string of digits and small English letters, length 1-6)
              type: "1" if the file contains an example test, "0" if regular test
        
    Returns:
        Tuple (min_lines, script), where:
        - min_lines: Minimum number of lines in the script
        - script: List of strings representing the move commands
    """
    pass
