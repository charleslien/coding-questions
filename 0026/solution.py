"""
Wet Shark asked Rat Kwesh to generate three positive real numbers x, y and z, from 0.1 to 200.0, inclusive. Wet Krash wants to impress Wet Shark, so all generated numbers will have exactly one digit after the decimal point.

Wet Shark knows Rat Kwesh will want a lot of cheese. So he will give the Rat an opportunity to earn a lot of cheese. He will hand the three numbers x, y and z to Rat Kwesh, and Rat Kwesh will pick one of the these twelve options:  a_1 = x^{y}^{z};  a_2 = x^{z}^{y};  a_3 = (x^{y})^{z};  a_4 = (x^{z})^{y};  a_5 = y^{x}^{z};  a_6 = y^{z}^{x};  a_7 = (y^{x})^{z};  a_8 = (y^{z})^{x};  a_9 = z^{x}^{y};  a_10 = z^{y}^{x};  a_11 = (z^{x})^{y};  a_12 = (z^{y})^{x}. 

Let m be the maximum of all the a_{i}, and c be the smallest index (from 1 to 12) such that a_{c} = m. Rat's goal is to find that c, and he asks you to help him. Rat Kwesh wants to see how much cheese he gets, so he you will have to print the expression corresponding to that a_{c}.

 


-----Input-----

The only line of the input contains three space-separated real numbers x, y and z (0.1 ≤ x, y, z ≤ 200.0). Each of x, y and z is given with exactly one digit after the decimal point.


-----Output-----

Find the maximum value of expression among x^{y}^{z}, x^{z}^{y}, (x^{y})^{z}, (x^{z})^{y}, y^{x}^{z}, y^{z}^{x}, (y^{x})^{z}, (y^{z})^{x}, z^{x}^{y}, z^{y}^{x}, (z^{x})^{y}, (z^{y})^{x} and print the corresponding expression. If there are many maximums, print the one that comes first in the list. 

x^{y}^{z} should be outputted as x^y^z (without brackets), and (x^{y})^{z} should be outputted as (x^y)^z (quotes for clarity). 


-----Examples-----
Input
1.1 3.4 2.5

Output
z^y^x

Input
2.0 2.0 2.0

Output
x^y^z

Input
1.9 1.8 1.7

Output
(x^y)^z
"""

def find_max_expression(x: float, y: float, z: float) -> str:
    """
    Find the maximum value among the twelve expressions and return the corresponding expression.
    
    Args:
        x: Real number with one digit after the decimal point (0.1 ≤ x ≤ 200.0)
        y: Real number with one digit after the decimal point (0.1 ≤ y ≤ 200.0)
        z: Real number with one digit after the decimal point (0.1 ≤ z ≤ 200.0)
        
    Returns:
        String representing the expression with the maximum value
    """
    pass
