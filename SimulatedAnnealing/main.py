import math
import random
import numpy as np

NODE_COUNT = 6
ITERATIONS = 1000000


def create_path() -> list:
    path = [n for n in range(NODE_COUNT)]
    path.append(0)
    return path

def create_matrix() -> list:
    return np.random.randint(1, 99, (NODE_COUNT, NODE_COUNT), "int64")

def swap(old_path: list) -> list:
    path = old_path.copy()

    x, y = random.sample(range(1, NODE_COUNT - 1), 2)
    path[x], path[y] = path[y], path[x]

    return path

def count(path: list, matrix: list) -> int:
    print("Path Length:")
    length = 0
    
    for i in range(len(path) - 1):
        length += matrix[path[i]][path[i + 1]]
        
        print(matrix[path[i]][path[i + 1]], end='')
        
        if i != len(path) - 2:
            print(" + ", sep='', end='')
        else:
            print(" = ", sep='', end='')
            
    print(length, '\n')
    return length

def main():
    temperature = 100
    path = create_path()
    matrix = create_matrix()
    
    print("Starting Path:", path)
    print("Starting Matrix:", matrix, "\n\n")
    
    len1 = count(path, matrix)
    
    for i in range(ITERATIONS):
        new_path = swap(path)
        print("Current Path:", new_path)
        
        len2 = count(new_path, matrix)
        diff = len2 - len1
        print("Difference of len1 and len2:", diff)
        
        if diff < 0:
            print("Accepting the path as new better path. (diff < 0)\n\n")
            path = new_path.copy()
            len1 = len2
        else:
            P = 100 * math.e ** (-diff / temperature)
            print("T =", temperature, "P = ", P)
            ratio = random.randint(0, 100)
            print("Generated ratio:", ratio)
            
            if P > ratio:
                print("Accepting the path as new better path. (P > ratio)\n\n")
                path = new_path.copy()
                len1 = len2
            else:
                print("Discarding this path\n\n")
        
        temperature /= 2
        if temperature <= 0.01: break
        
    print("Final path:", path)
    print("Final length:", len1)


if __name__ == "__main__":
    main()