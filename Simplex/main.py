import json


def get_data(path):
    with open(path, "r") as file:
        print("Loading table data\n")
        return json.load(file)
    
def fill_f_string(func: list, table: list):
    f_string = []
    
    for i in range(len(func)):
        d = 0
        
        for j in range(len(func)):
            d += 0 * table[i][j]

        print(f"Delta {i + 1}: {d - func[i]}")
        f_string.append(d - func[i])
        
    print("\n")
    return f_string

def optimal_check(f_string: list):
    for num in f_string:
        if num < 0:
            print(f"F-string of {f_string} is not optimal!\n")
            return False
    return True

def find_row(table: list, f_string: list):
    col = find_column(f_string, True)
    lowest = 9999
    table_index = 0
    a = []
    
    for row in table:
        a.append(row[-1] / row[col])
    
    for i in range(len(table)):
        if a[i] < lowest:
            lowest = a[i]
            table_index = i
            
    print(f"Pivot row: {table_index + 1}\n")
    return table_index

def find_column(f_string: list, silent: bool = False):
    table_index = f_string.index(min(f_string))
    
    if not silent:
        print(f"Pivot column: {table_index + 1}")
    return table_index

def swap_pivots(table: list, basis: list, func: list, column: int, row: int):
    basis[column] = func[row]
    print(f"Basis: {basis}")

def calc(table: list, f_string: list, basis: list, func: list):
    if not optimal_check(f_string):
        col = find_column(f_string)
        row = find_row(table, f_string)
        # Находим разрешающий элемент
        cross_element = table[row][col]
        print(f"Cross-element: a{col + 1}{row + 1} = {cross_element}")
        # находим значения по "правилу прямоугольника"
        for i in range(len(table)):
            if i == row: # пропускаем разрешающую строку
                continue
            for j in range(len(table) + 1):
                if j == col: # пропускаем разрешающий столбец
                    continue
                
                table[i][j] = (cross_element * table[i][j] - table[i][col] * table[row][j]) / cross_element
  
        for i in range(len(table) + 1):
            if i == col: # пропускаем разрешающий столбец
                    continue 
            
            try:
                f_string[i] = (cross_element * f_string[i] - f_string[col] * table[row][i]) / cross_element
            except IndexError:
                break;
        # делим значения строки на разрешающий элемент
        for i in range(len(table[row])):
            if i == col: # пропускаем разрешающий элемент
                continue;
            
            table[row][i] /= cross_element
        # делим значения столбца на разрешающий элемент и меняем знак
        for i in range(len(table[row][:-1])):
            if i == row: # пропускаем разрешающий элемент
                continue;
            
            table[i][col] /= -cross_element
            #print(table[i][col])
        f_string[col] /= -cross_element
        
        # меняем базис местами
        swap_pivots(table, basis, func, col, row)
        cross_element = 1 / cross_element # меняем элемент на обратный
        calc(table, f_string, basis, func)
    else:
        q = 0
        for i in range(len(basis)):
            q += basis[i] * table[i][-1]
        
        print("\nFinal table:\n{:<8} {:<8} {:<8} {:<8} {:<8}".format("", "x1", "x2", "x3", "A"))
        index = 4
        for v in table:
            print ("{:<8} {:<8} {:<8} {:<8} {:<8}".format("x"+str(index), round(v[0], 1), round(v[1], 1), round(v[2], 1), round(v[3], 1)))
            index += 1
        print ("{:<8} {:<8} {:<8} {:<8} {:<8}".format("F", round(f_string[0], 1), round(f_string[1], 1), round(f_string[2], 1), round(q, 1)))    

        
if __name__ == "__main__":    
    data = get_data("data.json")
    func = data["func"]
    table = data["table"]
    basis = [0, 0, 0]
    f_string = fill_f_string(func, table)
    
    calc(table, f_string, basis, func)
    