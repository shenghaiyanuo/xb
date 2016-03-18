def convert_querydict(querydict):
    convert_dict = dict(querydict)
    for i in convert_dict.keys():
        convert_dict[i] = ''.join(convert_dict[i])
    return convert_dict