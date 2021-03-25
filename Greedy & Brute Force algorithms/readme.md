# Application:

- A company wants to hire maximum number of people to increase the profit on a field based on limited budget (30000$).

## data:
| # of workers  | salary | Profit |
| ------------- | ------------- | ------------- |
| 13  | 1300$ | 12000  |
| 17  | 9805 | 10325  |
| 10  | 2931 | 17716  |
| 121  | 14693 | 50870  |
| 69  | 14137 | 43702  |
| 13  | 2674 | 7151  |
| 82  | 10325 | 59544  |
| 59  | 8297 | 29361  |
| 110  | 10471 | 38447  |
| 4  | 918 | 12000  |
| 126  | 14193 | 30000  |
| 42  | 14137 | 43702  |
| 102  | 2674 | 7151  |
| 64  | 10325 | 59544  |
| 93  | 8297 | 29361  |

## Algorithms:
For now two algorithms will be used 
- Greedy:
  - While threshold not reached add hire availabe workers.
- Brute force
  - enumerate all possible combinations of # of workers
  - Remove all combinations that exceed the budget threshold
  - From the remaining combinations, choose the # of workers with the highest profit

## Why using these algorithms:
- The above problem is a simple one that can be solved with even simpler model. However, if the application get complicated the models are still valid to be used
