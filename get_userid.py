def getUserids(result) :
    id_list = []
    for tweet in result :
        user_id = tweet['user']['screen_name']
        if not(user_id in id_list) : 
            id_list.append(user_id)

    return id_list
