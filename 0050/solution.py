"""
Welcome to Codeforces Stock Exchange! We're pretty limited now as we currently allow trading on one stock, Codeforces Ltd. We hope you'll still be able to make profit from the market!

In the morning, there are $n$ opportunities to buy shares. The $i$-th of them allows to buy as many shares as you want, each at the price of $s_i$ bourles.

In the evening, there are $m$ opportunities to sell shares. The $i$-th of them allows to sell as many shares as you want, each at the price of $b_i$ bourles. You can't sell more shares than you have.

It's morning now and you possess $r$ bourles and no shares.

What is the maximum number of bourles you can hold after the evening?


-----Input-----

The first line of the input contains three integers $n, m, r$ ($1 \leq n \leq 30$, $1 \leq m \leq 30$, $1 \leq r \leq 1000$) — the number of ways to buy the shares on the market, the number of ways to sell the shares on the market, and the number of bourles you hold now.

The next line contains $n$ integers $s_1, s_2, \dots, s_n$ ($1 \leq s_i \leq 1000$); $s_i$ indicates the opportunity to buy shares at the price of $s_i$ bourles.

The following line contains $m$ integers $b_1, b_2, \dots, b_m$ ($1 \leq b_i \leq 1000$); $b_i$ indicates the opportunity to sell shares at the price of $b_i$ bourles.


-----Output-----

Output a single integer — the maximum number of bourles you can hold after the evening.


-----Examples-----
Input
3 4 11
4 2 5
4 4 5 4

Output
26

Input
2 2 50
5 7
4 2

Output
50



-----Note-----

In the first example test, you have $11$ bourles in the morning. It's optimal to buy $5$ shares of a stock at the price of $2$ bourles in the morning, and then to sell all of them at the price of $5$ bourles in the evening. It's easy to verify that you'll have $26$ bourles after the evening.

In the second example test, it's optimal not to take any action.
"""

def max_bourles_after_trading(n: int, m: int, r: int, buy_prices: list, sell_prices: list) -> int:
    """
    Calculate the maximum number of bourles you can hold after the evening.
    
    Args:
        n: Number of ways to buy shares (1 ≤ n ≤ 30)
        m: Number of ways to sell shares (1 ≤ m ≤ 30)
        r: Number of bourles you hold initially (1 ≤ r ≤ 1000)
        buy_prices: List of n integers representing prices to buy shares (1 ≤ s_i ≤ 1000)
        sell_prices: List of m integers representing prices to sell shares (1 ≤ b_i ≤ 1000)
        
    Returns:
        Maximum number of bourles you can hold after the evening
    """
    pass
