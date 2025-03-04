"""
Petya recieved a gift of a string s with length up to 10^5 characters for his birthday. He took two more empty strings t and u and decided to play a game. This game has two possible moves:  Extract the first character of s and append t with this character.  Extract the last character of t and append u with this character. 

Petya wants to get strings s and t empty and string u lexicographically minimal.

You should write a program that will help Petya win the game.


-----Input-----

First line contains non-empty string s (1 ≤ |s| ≤ 10^5), consisting of lowercase English letters.


-----Output-----

Print resulting string u.


-----Examples-----
Input
cab

Output
abc

Input
acdb

Output
abdc
"""

def lexicographically_minimal_string(s: str) -> str:
    """
    Determine the lexicographically minimal string u that can be obtained
    by performing a sequence of the two allowed moves.
    
    Args:
        s: Non-empty string consisting of lowercase English letters (1 ≤ |s| ≤ 10^5)
        
    Returns:
        The lexicographically minimal string u
    """
    pass
