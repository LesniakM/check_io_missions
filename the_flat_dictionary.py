flatten_dict = {}


def add_key(key_string, value):
    # This function is used just to workaround empty values and give key_miner access to output dictionary.

    global flatten_dict
    if value != {}:
        flatten_dict[key_string] = value
    else:
        flatten_dict[key_string] = ""


def key_miner(keys, dictionary, nest_string=""):
    # This recursive function checks, if key have just value or another nested dict.
    # If for given key there is just normal value, it saves it to output dictionary.
    # If for given key there is nested dict, it run itself with additional information about
    # previously used keys (nested_string).

    for key in keys:
        if ": " not in str(dictionary[key]):
            if nest_string:
                add_key(f"{nest_string}{key}", dictionary[key])
            else:
                add_key(key, dictionary[key])
        else:
            nested_string = nest_string + key + "/"
            child_keys = list(dictionary[key].keys())
            key_miner(child_keys, dictionary[key], nested_string)


def flatten(dictionary):
    global flatten_dict
    flatten_dict = {}
    root_keys = list(dictionary.keys())
    key_miner(root_keys, dictionary)
    return flatten_dict


if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
        "first": "One",
        "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}

    print('You all set. Click "Check" now!')
