users = ["Asha", "Ben", "Carlos", "Divya"]

# matrix[i][j] = 1 means users[i] and users[j] are friends
friendship_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
]


def are_friends(user1, user2):
    """Check whether two users are directly connected."""
    if user1 not in users or user2 not in users:
        return False

    i = users.index(user1)
    j = users.index(user2)
    return friendship_matrix[i][j] == 1


def display_matrix():
    """Print the matrix with user names."""
    print("     " + " ".join(f"{user:>8}" for user in users))
    for i, user in enumerate(users):
        row = " ".join(f"{value:>8}" for value in friendship_matrix[i])
        print(f"{user:>5} {row}")


display_matrix()

first_user = "Asha"
second_user = "Ben"

if are_friends(first_user, second_user):
    print(f"\n{first_user} and {second_user} are friends.")
else:
    print(f"\n{first_user} and {second_user} are not friends.")