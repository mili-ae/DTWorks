import json


def get_data_table():
    with open("table.json") as f:
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

def alternative(kn: list):
    a = []
    w = []

    for key, element in get_data_table().items():
        if key != "k0":
            a.append(priority(element))

    for i in range(len(kn)):
        wi = 0
        for j in range(len(kn)):
            wi += kn[j] * a[i][j]

        w.append(wi)

    return w


if __name__ == "__main__":
    # If you see this comment you've been rickrolled
    for key, table in get_data_table().items():
        print(f"{key}: ", priority(table))
    
    print(alternative(priority(get_data_table()["k0"])))
