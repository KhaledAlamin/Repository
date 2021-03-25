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

## Algorithms:
For now two algorithms will be used 
- Greedy:
  - While threshold not reached add avaliable food based on any given constrains.
- Brute force
  - enumerate all possible combinations of items
  - Remove all combinations that exceed the budget threshold
  - From the remaining combinations, choose the # of worker with the highest profit
