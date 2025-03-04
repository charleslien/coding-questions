"""
Vasiliy has a car and he wants to get from home to the post office. The distance which he needs to pass equals to d kilometers.

Vasiliy's car is not new — it breaks after driven every k kilometers and Vasiliy needs t seconds to repair it. After repairing his car Vasiliy can drive again (but after k kilometers it will break again, and so on). In the beginning of the trip the car is just from repair station.

To drive one kilometer on car Vasiliy spends a seconds, to walk one kilometer on foot he needs b seconds (a < b).

Your task is to find minimal time after which Vasiliy will be able to reach the post office. Consider that in every moment of time Vasiliy can left his car and start to go on foot.


-----Input-----

The first line contains 5 positive integers d, k, a, b, t (1 ≤ d ≤ 10^12; 1 ≤ k, a, b, t ≤ 10^6; a < b), where:  d — the distance from home to the post office;  k — the distance, which car is able to drive before breaking;  a — the time, which Vasiliy spends to drive 1 kilometer on his car;  b — the time, which Vasiliy spends to walk 1 kilometer on foot;  t — the time, which Vasiliy spends to repair his car. 


-----Output-----

Print the minimal time after which Vasiliy will be able to reach the post office.


-----Examples-----
Input
5 2 1 4 10

Output
14

Input
5 2 1 4 5

Output
13



-----Note-----

In the first example Vasiliy needs to drive the first 2 kilometers on the car (in 2 seconds) and then to walk on foot 3 kilometers (in 12 seconds). So the answer equals to 14 seconds.

In the second example Vasiliy needs to drive the first 2 kilometers on the car (in 2 seconds), then repair his car (in 5 seconds) and drive 2 kilometers more on the car (in 2 seconds). After that he needs to walk on foot 1 kilometer (in 4 seconds). So the answer equals to 13 seconds.
"""

def min_time_to_post_office(d: int, k: int, a: int, b: int, t: int) -> int:
    """
    Calculate the minimal time after which Vasiliy will be able to reach the post office.
    
    Args:
        d: Distance from home to the post office (1 ≤ d ≤ 10^12)
        k: Distance the car can drive before breaking (1 ≤ k ≤ 10^6)
        a: Time to drive 1 kilometer by car (1 ≤ a ≤ 10^6)
        b: Time to walk 1 kilometer on foot (1 ≤ b ≤ 10^6, a < b)
        t: Time to repair the car (1 ≤ t ≤ 10^6)
        
    Returns:
        Minimal time to reach the post office
    """
    pass
