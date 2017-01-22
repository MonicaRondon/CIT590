with open("city-data.txt", "r") as stream:
    lines = stream.read()
    lines.strip().split("\t")
    
print(lines)
