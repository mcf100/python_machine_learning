is_raining = True
is_windy = False

stay_inside = is_raining and is_windy
print(f"Stay inside: {stay_inside}")

take_coat = is_raining or is_windy
print(f"Take a coat: {take_coat}")

print(f"Not windy: {not is_windy}")

take_umbrella = is_raining and not is_windy
print(f"Take umbrella: {take_umbrella}")