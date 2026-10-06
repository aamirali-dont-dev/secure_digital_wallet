# Secure Digital Wallet

A console-based digital wallet system written in Python for **Assignment 1** of *Introduction to Object Oriented Programming* (BS Financial Technology, Government College University, Lahore).

**Author:** Aamir Ali | **Roll No:** 6911-BS-FT-24

**Public repository:** https://github.com/aamirali-dont-dev/secure_digital_wallet
The commit history there shows the program being built in stages.

---

## Observations

**What I built and how.** I developed the program in small stages and committed after each one: constructor, getters and display, deposit and withdraw, transfer, the history display, and the wallet dictionary with search, followed by the demo. The commit history in the repository shows that order.

**Design choices**

- **Negative opening balance.** I chose to print a warning and set the balance to 0 rather than raise an error, so the program keeps running. In a real financial system, raising an error might be better, because silently correcting input can hide mistakes.
- **Checks before changes.** Every validation in `transfer` runs before any balance changes. That way a failed transfer cannot leave one wallet debited and the other not credited.
- **Records written by hand in `transfer`.** Reusing `withdraw` and `deposit` would have saved code, but the histories would then say "Withdrawal" and "Deposit" instead of showing where the money went. I wrote the records inside `transfer` so each side shows the other wallet's ID. This works because private attributes are private to the class, not to a single object, so a method can update another `DigitalWallet` without any outside code touching private data.
- **Return values.** `deposit`, `withdraw`, and `transfer` return `True` or `False`, so calling code knows whether an operation worked.
- **Copy of the history.** Returning a copy means appending to or clearing the returned list leaves the wallet's real history unchanged. The demo tests this directly.

**Problems I ran into and fixed**

- A negative opening balance printed a message but never set the balance, so the attribute did not exist. Every path now assigns it.
- In `transfer`, the transaction counter was increased before the record was written, which skipped ID 2 on the sender and started the receiver at ID 2. I made it match `deposit` and `withdraw` (record first, then increment).
- Wrapping `display_wallet()` in `print` produced a stray `None` (and later a duplicate line), because the method already prints its own output. It is now called directly.
- The history header was printed inside the loop, so it repeated for every transaction. It now prints once, above the loop.

**Limitations and possible improvements**

- Transactions are stored as formatted strings, which are easy to print but hard to filter or total. Storing each one as a dictionary (type, amount, balances) would allow searching and reporting.
- Amounts are not checked to be numbers, so passing text would cause an error.
- Wallets are created and added to the dictionary by hand. A helper function that creates a wallet and files it in `wallets` in one step, with a duplicate-ID check, would be safer.
- The program has no persistence. All data is lost when it ends. Saving wallets to a file or database would fix that.

---

## Project Overview

The program models wallets as objects, protects their balances through encapsulation, and manages several wallets and their transaction histories using Python lists and a dictionary.

### Concepts Demonstrated

| Concept | Where it appears |
|---|---|
| Classes, objects, constructor | `DigitalWallet` and its `__init__` |
| Encapsulation / information hiding | Private `__balance`, `__transaction_history`, `__transaction_id` |
| Abstraction | Public methods (`deposit`, `withdraw`, `transfer`, getters) hide the internal logic |
| Lists | Per-wallet transaction history |
| Dictionaries | `wallets` dictionary mapping wallet ID to wallet object |
| Input validation | Zero, negative, insufficient-funds, and invalid-receiver checks |

### Project Structure

```
secure_digital_wallet/
├── wallet.py        # the full program: class, wallet dictionary, and demo
├── README.md        # this file
├── .gitignore
└── (screenshots of the program output)
```

### How to Run

Requires Python 3.

```bash
python wallet.py
```

The demo at the bottom of the file runs automatically and prints the result of every scenario.

## The `DigitalWallet` Class

**Attributes**

- `wallet_id`: public identifier of the wallet
- `owner_name`: public name of the owner
- `__balance`: private balance
- `__transaction_history`: private list of transaction records
- `__transaction_id`: private counter used to number each wallet's transactions

**Methods**

| Method | Purpose |
|---|---|
| `get_balance()` | Returns the current balance |
| `get_transaction_history()` | Returns a **copy** of the history, so outside code cannot change the original |
| `display_wallet()` | Prints the wallet ID, owner name, and balance |
| `deposit(amount)` | Adds money after validating the amount |
| `withdraw(amount)` | Removes money after validating the amount and checking funds |
| `transfer(amount, receiver_wallet)` | Moves money to another wallet and records it in both histories |
| `Full_Transaction_History()` | Loops through and prints every transaction in the wallet |

## Validation Rules

- The opening balance cannot be negative. A negative value prints a warning and the balance is set to 0.
- Zero or negative amounts are rejected for deposits, withdrawals, and transfers.
- Withdrawals and transfers larger than the balance are rejected as insufficient funds.
- A transfer is rejected if the receiver is not a `DigitalWallet`, or is the same wallet as the sender.
- A rejected operation changes no balance and adds no history record.

## Transaction Records

Every successful operation adds one record to the wallet's history containing the transaction ID, nature (`Cr` for credit, `Dr` for debit), previous balance, the amount, and the new balance. Transfers also record the other wallet's ID, and they write a record in **both** the sender's and the receiver's history.

## Wallet Collection

Three wallets are stored in a dictionary named `wallets`, keyed by wallet ID:

| ID | Owner | Opening balance |
|---|---|---|
| 001 | Saboor | 1000 |
| 002 | Ali | 500 |
| 003 | Danika | 2000 |

- `display_all_wallets()` loops over the dictionary and displays every wallet.
- `search_walletid(wallet_id)` looks a wallet up by ID and prints a clear message if the ID does not exist.

## Demo Scenarios

The program demonstrates:

1. Starting state of all wallets
2. A successful deposit and rejected deposits (zero, negative)
3. A successful withdrawal and rejected withdrawals (insufficient funds, zero, negative)
4. A successful transfer and rejected transfers (insufficient funds, zero, negative, same wallet, not a wallet)
5. Withdrawing the exact balance (boundary case)
6. Wallet search: one ID that exists and one that does not
7. Encapsulation: the history returned by the getter is a copy, so changing it leaves the original untouched
8. Constructor validation (negative opening balance) and the empty-history message
9. Full transaction history of each wallet
10. Final balances

**Expected final state**

| Wallet | Final balance | History records |
|---|---|---|
| 001 Saboor | 1200 | 2 (deposit, transfer out) |
| 002 Ali | 0 | 2 (two withdrawals) |
| 003 Danika | 2300 | 1 (transfer in) |

Screenshots of the program output are included in this repository and in the submitted ZIP.