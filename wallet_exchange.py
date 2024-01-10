'''
A. Wallet Exchange
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Alice and Bob are bored, so they decide to play a game with their wallets. Alice has a
 coins in her wallet, while Bob has b
 coins in his wallet.

Both players take turns playing, with Alice making the first move. In each turn, the player will perform the following steps in order:

Choose to exchange wallets with their opponent, or to keep their current wallets.
Remove 1
 coin from the player's current wallet. The current wallet cannot have 0
 coins before performing this step.
The player who cannot make a valid move on their turn loses. If both Alice and Bob play optimally, determine who will win the game.

Input
Each test contains multiple test cases. The first line contains a single integer t
 (1≤t≤1000
) — the number of test cases. The description of the test cases follows.

The first and only line of each test case contains two integers a
 and b
 (1≤a,b≤109
) — the number of coins in Alice's and Bob's wallets, respectively.

Output
For each test case, output "Alice" if Alice will win the game, and "Bob" if Bob will win the game.
'''


if __name__ == '__main__':
    t = int(input().strip())

    for i in range(t):
        a, b = map(int, input().rstrip().split())
        if (a + b) % 2:
            print('Alice')
        else:
            print('Bob')