import json

weight = [5, 2, 4, 4, 3]
tend = [True, False, False, True, False]

def get_data_table():
    with open("table.json") as f:
        data = json.load(f)
    
    return data

def translate(data: dict):
    mod_data = {
        "1CDev"    :   [],
        "WebDev"   :   [],
        "BitrixDev"    :   [],
        "JavaDev"  :   [],
        "VBSQLDev"  :   [],
        "SeniorPHPDev"  :   [],
        "LeadAndroidDev"    :   [],
        "iOSAndroidDev" :   [],
        "Devops"    :   []
    }

    # What the fuck is this?
    # Idk, but let's not touch it, okay?
    for job in data:
        for element in data[job]:
            if element == "salary":
                if data[job][element] <= 100:
                    mod_data[job].append(1)
                elif data[job][element] > 100 and data[job][element] <= 200:
                    mod_data[job].append(2)
                else:
                    mod_data[job].append(3)

            if element == "distance":
                if data[job][element] == 0:
                    mod_data[job].append(0)
                elif data[job][element] > 0 and data[job][element] <= 0.3:
                    mod_data[job].append(3)
                elif data[job][element] > 0.3 and data[job][element] <= 0.4:
                    mod_data[job].append(4)
                elif data[job][element] > 0.4 and data[job][element] <= 0.5:
                    mod_data[job].append(5)
                else:
                    mod_data[job].append(6)

            if element == "exp":
                if data[job][element] >= 3:
                    mod_data[job].append(3)
                else:
                    mod_data[job].append(data[job][element])

            if element == "education":
                mod_data[job].append(data[job][element])

            if element == "worktime":
                if data[job][element] == 0:
                    mod_data[job].append(0)
                elif data[job][element] < 8:
                    mod_data[job].append(5)
                else:
                    mod_data[job].append(8)

    return mod_data   

def compare(job: list, to_job: list):
    pros = 0
    cons = 0

    for i in range(len(job)):
        if tend[i] and job[i] != to_job[i]:
            if job[i] > to_job[i]:
                pros += weight[i]
            else:
                cons += weight[i]
        else:
            if job[i] != to_job[i]:
                if job[i] < to_job[i]:
                    pros += weight[i]
                else:
                    cons += weight[i]
    
    if cons != 0:
        return pros / cons

    if pros != 0:
        return 100
    return 0
    
def electra2(limit: int):
    tr_data = translate(get_data_table())
    to_ret = []

    for job in tr_data:
        for to_job in tr_data:
            
            if job != to_job and compare(tr_data[job], tr_data[to_job]) > limit:
                to_ret.append((job, compare(tr_data[job], tr_data[to_job]), to_job))

    return to_ret
if __name__ == "__main__":
    # If you see this comment you've been rickrolled
    #print(translate(get_data_table()))
    print(electra2(5))