import facebook

token = ""

graph = facebook.GraphAPI(access_token=token,
                          version="2.10")


def get_friend_count(the_id):
    friends = graph.get_object('%s/friends' % the_id)

    # return friend count.
    if 'summary' not in friends:
        return 0
    return friends['summary'].get('total_count', 0)


def get_all_friends(the_id):
    after = ''
    all_friends = []

    while True:
        friends = graph.get_object('%s/friends' % the_id,
                                   after=after)
        if not friends['data']:
            # no more friends. :(
            break

        all_friends += friends['data']
        after = friends['paging']['cursors']['after']

    return all_friends


def get_my_top_friends():
    all_my_sobolans = get_all_friends('me')

    # Creating a list of (friend, friend's friend count)
    friends = {}
    for sobolan in all_my_sobolans:
        friends_total_friends = get_friend_count(
            sobolan['id'])
        friends[sobolan['name']] = friends_total_friends

    # sort the friends by sobolan count.
    # sorted_friends = sorted(sobolan,
    #                         lambda x, y: x.values()[0] > y.values()[0])

    # return sorted_friends[0:5]


get_my_top_friends()
