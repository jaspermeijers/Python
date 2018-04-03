def new_password(oldpassword, newpassword):
    'voer oude password in, voer nieuwe password in ' ''
    if oldpassword == newpassword:
        return('False')
    if len(newpassword) > 6:
        return('True')

print(new_password('geoictstudent', 'geoictstudent'))