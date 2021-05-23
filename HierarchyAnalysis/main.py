import json


def get_data_table():
    with open("HierarchyAnalysis/table.json") as f:
        data = json.load(f)
    
    return data

def priority(data: list):
    sumv = 0
    v = []
    w = []

    for row in data:
        vi = 1
        for element in row:
            vi *= element

        v.append(pow(vi, 1/len(data)))
        sumv += pow(vi, 1/len(data))
         
    for i in v:
        w.append(i / sumv)

    return w

def local_priority_check(table: list):
    s = []
    p = []
    w = priority(table)

    for i in range(len(table)):
        si = 0
        for j in range(len(table)):
            si += table[j][i]
        
        s.append(si)

    for i in range(len(s)):
        p.append(s[i] * w[i])

    amax = sum(p)
    indP = (amax - len(table)) / (len(table) - 1)
    cr = indP / 1.12
    
    if cr > 0.10:
        print(cr, "> 0.10")
        exit(0)

def alternative(kn: list):
    best = 0
    a = []
    # w = []

    for key, element in get_data_table().items():
        if key != "k0":
            a.append(priority(element))

    for i in range(len(kn)):
        wi = 0
        for j in range(len(kn)):
            wi += kn[j] * a[i][j]

        if best < wi:
            best = wi

        # w.append(wi)

    return best


if __name__ == "__main__":
    # If you see this comment you've been rickrolled
    for key, table in get_data_table().items():
        print(f"{key}: ", priority(table))

    for key, table in get_data_table().items():
        local_priority_check(table)
    
    print(alternative(priority(get_data_table()["k0"])))
