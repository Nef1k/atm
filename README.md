# ATM

Provides web version of a simple ATM. After you start this just go to root and start clicking.

## Applications

* core - contains all common templates, error page, static files and fixtures
* auth_core - provides authorization service. Contains `Card` and `AuthAttempt` models.
* operations - provides two operations: balance check and withdrawal. Contains `Operation` and `OperationType` models

## Files

* `requirements.txt` - all the dependencies neede
* `core/fixtures/test.fixture` - test data for... tests

## Test data
Few card numbers with pins goes next

| Card Number     | Pin  | Is active |
| --------------- |:----:| ---------:|
| 111111111111111 | 4567 | True      |
| 132456789101112 | 0132 | False     |
| 654789461365765 | 9806 | True      |

Here'e a [GitHub repo](https://github.com/Nef1k/atm/)
