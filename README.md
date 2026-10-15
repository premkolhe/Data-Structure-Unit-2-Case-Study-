# Data-Structure-Unit-2-Case-Study-
A Python case study demonstrating how an adjacency matrix represents friendship connections in a social network, with a function to check whether two users are directly connected. Includes a discussion of time complexity and memory limitations for large, sparse networks.

## How It Works

Each row and column represents a user:

- `1` means the two users are friends.
- `0` means they are not directly connected.
- The diagonal contains `0` because a user is not listed as their own friend.
- The matrix is symmetric because friendships are mutual in this example.

## Example Network

The example uses four users: Asha, Ben, Carlos, and Divya. The program prints their friendship matrix and checks whether Asha and Ben are friends.

## Requirements

- Python 3.7 or newer
- No external packages required

## How to Run

Open a terminal in this folder and run:

```bash
python CaseStudy2.py