import csv
def read_csv(a):
    file = open(a)
    csvreader = csv.reader(file)
    return csvreader
def write_csv(a,rows):
    file = open(a, "w")
    csvwriter = csv.writer(file)
    csvwriter.writerows(rows)
def hiest_csv(a):
    h={}
    csvreader = read_csv(a)
    for i in csvreader:
        if i[2].isdigit():
            h[i[0]] = i[2]
    fin_max=max(h,key=h.get)
    print(fin_max)
def lovest_csv(a):
    h={}
    csvreader = read_csv(a)
    for i in csvreader:
        if i[2].isdigit():
            h[i[0]] = i[2]
    fin_min = min(h, key=h.get)
    print(fin_min)
def average(a):
    h = 0
    count=1
    csvreader = read_csv(a)
    for i in csvreader:
        if i[2].isdigit():
            h+=int(i[2])
            count+=1
    print(h/count)

def print_csv(a):
    csvreader=read_csv(a)
    for row in csvreader:
        print(" ".join(row))





