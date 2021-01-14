example = {
    'data': {
        'name': 'ignacio',
        'age': 36
    },
    'social': {
        'feed': 'facebook'
    }
}

for index, [key, dic] in enumerate(example.items()):
    print(index, key, dic)
