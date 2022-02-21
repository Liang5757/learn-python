users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'paris',
    },                                      #字典结束后加逗号

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tlocation: " + location.title())