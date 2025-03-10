"""
Now you can take online courses in the Berland State University! Polycarp needs to pass k main online courses of his specialty to get a diploma. In total n courses are availiable for the passage.

The situation is complicated by the dependence of online courses, for each course there is a list of those that must be passed before starting this online course (the list can be empty, it means that there is no limitation).

Help Polycarp to pass the least number of courses in total to get the specialty (it means to pass all main and necessary courses). Write a program which prints the order of courses. 

Polycarp passes courses consistently, he starts the next course when he finishes the previous one. Each course can't be passed more than once. 


-----Input-----

The first line contains n and k (1 ≤ k ≤ n ≤ 10^5) — the number of online-courses and the number of main courses of Polycarp's specialty. 

The second line contains k distinct integers from 1 to n — numbers of main online-courses of Polycarp's specialty. 

Then n lines follow, each of them describes the next course: the i-th of them corresponds to the course i. Each line starts from the integer t_{i} (0 ≤ t_{i} ≤ n - 1) — the number of courses on which the i-th depends. Then there follows the sequence of t_{i} distinct integers from 1 to n — numbers of courses in random order, on which the i-th depends. It is guaranteed that no course can depend on itself. 

It is guaranteed that the sum of all values t_{i} doesn't exceed 10^5. 


-----Output-----

Print -1, if there is no the way to get a specialty. 

Otherwise, in the first line print the integer m — the minimum number of online-courses which it is necessary to pass to get a specialty. In the second line print m distinct integers — numbers of courses which it is necessary to pass in the chronological order of their passage. If there are several answers it is allowed to print any of them.


-----Examples-----
Input
6 2
5 3
0
0
0
2 2 1
1 4
1 5

Output
5
1 2 3 4 5 

Input
9 3
3 9 5
0
0
3 9 4 5
0
0
1 8
1 6
1 2
2 1 2

Output
6
1 2 9 4 5 3 

Input
3 3
1 2 3
1 2
1 3
1 1

Output
-1



-----Note-----

In the first test firstly you can take courses number 1 and 2, after that you can take the course number 4, then you can take the course number 5, which is the main. After that you have to take only the course number 3, which is the last not passed main course.
"""

def min_courses_to_pass(n: int, k: int, main_courses: list, dependencies: list) -> tuple:
    """
    Calculate the minimum number of courses Polycarp needs to pass to get his specialty
    and the order in which he should take them.
    
    Args:
        n: Number of online courses (1 ≤ k ≤ n ≤ 10^5)
        k: Number of main courses (1 ≤ k ≤ n ≤ 10^5)
        main_courses: List of k distinct integers from 1 to n representing main courses
        dependencies: List of n lists, where dependencies[i-1] represents the courses
                     that must be passed before course i
        
    Returns:
        If there is no way to get a specialty, return (-1, [])
        Otherwise, return (m, courses), where:
        - m is the minimum number of courses to pass
        - courses is a list of m distinct integers representing the courses to pass
          in chronological order
    """
    pass
