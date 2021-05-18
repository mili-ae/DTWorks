import json


def get_data_table():
    with open("table.json") as f:
        data = json.load(f)
    
    return data

def compare(job, to_job):
    return (job[0] >= to_job[0] and 
            job[1] <= to_job[1] and 
            job[2] <= to_job[2] and 
            job[3] >= to_job[3] and 
            job[4] <= to_job[4])

def pareto_func(data: dict):
    to_ret = []

    for job in list(data):
        for job2 in list(data):
            if data[job] != data[job2] and compare(data[job], data[job2]):
                if job not in to_ret: to_ret.append(job) 

        # Python 3 doesn't allow to delete keys while iterating, so i have to use this hacky solution. H-A-C-K-E-R-M-A-N
        to_del = [key for key in data if key == job]
        for key in to_del: del data[key]

    return to_ret

def criteria_choice(data: dict):
    for key, item in list(data.items()):
        try:
            if item[0] < 150:
                del data[key]
            if item[2] > 1:
                del data[key]
        except KeyError: # Oh no. Anyways
            pass

    return data

def sub_opt(data: dict):
    best = list(data)[0]

    for key in data:
        if data[best][0] < data[key][0] and data[best] != data[key]:
            best = key
            
    return best

def lex_opt(data: dict):
    best = []

    # 1: Education
    for key in data:
        if data[key][3] == 2:
            best.append(key)


    while len(best) != 1:
        # 2: Salary
        for key in best:
            for key2 in best:
                if key != key2 and data[key][0] > data[key2][0]:
                    best.remove(key2)
        # 3: Work Experience
        for key in best:
            for key2 in best:
                if key != key2 and data[key][2] < data[key2][2]:
                    best.remove(key2)
        # 4: Workday time
        for key in best:
            for key2 in best:
                if key != key2 and data[key][4] < data[key2][4]:
                    best.remove(key2)

        # 5: Distance from home
        for key in best:
            for key2 in best:
                if key != key2 and data[key][1] < data[key2][1]:
                    best.remove(key2)

    return best[0]


if __name__ == "__main__":
    # If you see this comment you've been rickrolled
    print("Парето-доминирование: ", pareto_func(get_data_table()))
    print("\nМетод сужения: ", criteria_choice(get_data_table()))
    print("\nМетод субоптимизации: ",sub_opt(criteria_choice(get_data_table())))
    print("\nЛексикографическая оптимизация: ", lex_opt(get_data_table()))
