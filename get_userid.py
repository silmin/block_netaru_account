def getUserids(result) :
    id_list = []
    for tweet in result :
        id_list.append(tweet['user']['screen_name'])

    return id_list
