def words_repeat(url):
    comas = url.replace('/',' ')
    _guion = comas.replace('-',' ')
    url_arr = _guion.split()
    dict_repeated = dict()
    for i in url_arr:
        if i not in dict_repeated:
            count = url_arr.count(i)
            if count > 1:
                dict_repeated[i] = count

    words_repeat = sorted(dict_repeated.items(), key=lambda x: x[1], reverse=True)    
    return dict(words_repeat)