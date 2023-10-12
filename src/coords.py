coords = [526, -589, 260, -93, 62, 177]
# randomize the first 3 coords within 10 of the original
coords[0] = random.randint(coords[0] - 10, coords[0] + 10)
coords[1] = random.randint(coords[1] - 10, coords[1] + 10)
coords[2] = random.randint(coords[2] - 10, coords[2] + 10)

print(coords)