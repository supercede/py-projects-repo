"""
* Ask user for 3 friends names
* Check if friends are close by (in friends.txt)
* If friends are nearby, save to nearby_friends.txt)
"""

my_friends_list = open('friends.txt', 'r')
friends = [line.strip().lower() for line in my_friends_list.readlines()]
my_friends_list.close()

print(friends)


def createFriendsList():
    user_friends = []

    while len(user_friends) < 3:
        friend = input(
            f"Enter 3 friends names. Friend {len(user_friends) + 1}: ")
        user_friends.append(friend)
    check_friend(user_friends)


def check_friend(friend_list):
    friends_set = set(friends)
    nearby_friends_list = set([friend.lower() for friend in friend_list])
    nearby_friends = friends_set.intersection(nearby_friends_list)

    save_to_file(nearby_friends)


def save_to_file(list):
    nearby_friends = open('nearby_friends.txt', 'w')
    str_list = '\n'.join(list)
    nearby_friends.write(str_list)

    nearby_friends.close()


createFriendsList()
