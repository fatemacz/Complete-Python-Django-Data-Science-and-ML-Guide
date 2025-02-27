import csv

with open("test.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=";")
    writer.writerow(["user_id", "user_name", "comments_qty"])
    writer.writerow([5423, "Aye", 1300])
    writer.writerow([5425, "alice", 830])
    writer.writerow([7245, "bob", 970])

with open("test.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=";")
    for index, line in enumerate(reader):
        print(index, line)
        if index == 0:
            header = line
        else:
            for idx, val in enumerate(line):
                print(f"{header[idx]}: {val}")
