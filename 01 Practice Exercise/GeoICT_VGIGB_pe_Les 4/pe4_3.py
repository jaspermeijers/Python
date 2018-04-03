def lang_genoeg(lengte):
    'voer lengte in CM in'
    if lengte >= 120:
        return ('Je bent lang genoeg voor de attractie!')
    else:
        return ('Sorry, je bent te klein!')

print(lang_genoeg(120))