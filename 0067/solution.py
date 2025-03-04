"""
Limak is a little polar bear. He has a favorite triangle with vertices at points (a, 0), (0, b) and (0, 0), where a and b are positive integers. Limak wants to know the area of his triangle.

But Limak is a lazy bear. He doesn't want to compute the area by himself. He asked his friend Radewoosh to help him. Radewoosh is a deer and he doesn't know much about triangles. He knows that the area of a triangle can be computed as 1/2 of the absolute value of the cross product of two vectors.

Radewoosh chose vectors (a, 0) and (0, b) and computed the area as 1/2 of the absolute value of their cross product. Limak is not sure if Radewoosh's approach is correct. He asks you to compute the area of his triangle.


-----Input-----

The only line of the input contains two integers a and b (1 ≤ a, b ≤ 100) — the coordinates of the vertices of Limak's triangle.


-----Output-----

Print one character:
- "+" if Radewoosh's result is greater than the actual area of the triangle.
- "-" if Radewoosh's result is smaller than the actual area of the triangle.
- "0" if Radewoosh's result is equal to the actual area of the triangle.
- "?" if you can't determine the relation between Radewoosh's result and the actual area of the triangle.


-----Examples-----
Input
3 7

Output
-

Input
2 0

Output
?

Input
1 1

Output
0
"""

def compare_triangle_areas(a: int, b: int) -> str:
    """
    Compare Radewoosh's calculated area with the actual area of Limak's triangle.
    
    Args:
        a: x-coordinate of the first vertex (1 ≤ a ≤ 100)
        b: y-coordinate of the second vertex (1 ≤ b ≤ 100)
        
    Returns:
        "+" if Radewoosh's result is greater than the actual area
        "-" if Radewoosh's result is smaller than the actual area
        "0" if Radewoosh's result is equal to the actual area
        "?" if the relation cannot be determined
    """
    pass
