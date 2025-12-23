import math
import sys
sys.set_int_max_str_digits(0)

def check_regularity(data, n):
    unique = set(data)
    if len(unique) != n ** 3:
        print(f"Error: Duplicate elements found! (Unique: {len(unique_elements)})")
        return

    min_val = min(unique)
    max_val = max(unique)

    if min_val == 0 and max_val == n ** 3 - 1:
        print(f"Normal (0 to {max_val})")
    elif min_val == 1 and max_val == n ** 3:
        print(f"Normal (1 to {max_val})")
    else:
        print(f"Non-normal (Range: {min_val} to {max_val})")


data = []
fname = input("Input file name: ")

try:
    with open(fname, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(',')
            for p in parts:
                val = p.strip()
                if val:
                    data.append(int(val))

    N = 1
    while N**3 < len(data):
        N += 1
    if N ** 3 != len(data):
        print(f"Error: {len(data)} is not cube")
    else:
        print(f"{N}*{N}*{N} Cube")
        check_regularity(data, N)
        k = 1
        while(1):
            semimagic = True
            diag = True
            sum = 0
            for i in range(N):
                sum += data[i] ** k
            for x in range(N):
                if not semimagic:
                    break;
                for y in range(N):
                    s = 0
                    for z in range(N):
                        s += data[x + y*N + z*N*N] ** k
                    if s != sum:
                        semimagic = False
                        break
            for x in range(N):
                if not semimagic:
                    break;
                for z in range(N):
                    s = 0
                    for y in range(N):
                        s += data[x + y*N + z*N*N] ** k
                    if s != sum:
                        semimagic = False
                        break
            for y in range(N):
                if not semimagic:
                    break;
                for z in range(N):
                    s = 0
                    for x in range(N):
                        s += data[x + y*N + z*N*N] ** k
                    if s != sum:
                        semimagic = False
                        break
            s = 0
            for i in range(N):
                s += data[i + i*N + i*N*N] ** k
            if s != sum:
                diag = False
            s = 0
            for i in range(N):
                s += data[i + i*N + (N-1-i)*N*N] ** k
            if s != sum:
                diag = False
            s = 0
            for i in range(N):
                s += data[i + (N-1-i)*N + i*N*N] ** k
            if s != sum:
                diag = False
            s = 0
            for i in range(N):
                s += data[i + (N-1-i)*N + (N-1-i)*N*N] ** k
            if s != sum:
                diag = False
            if semimagic or diag:
                label = f"S{k}"
                if not diag:
                    label += "(semimagic)"
                print(f"{label}={sum}")
            k += 1
            if not semimagic:
                break


        semimagic = True
        diag = True
        product = 1
        for i in range(N):
            product *= data[i]
        for x in range(N):
            if not semimagic:
                break;
            for y in range(N):
                p = 1
                for z in range(N):
                    p *= data[x + y*N + z*N*N]
                if p != product:
                    semimagic = False
                    break
        for x in range(N):
            if not semimagic:
                break;
            for z in range(N):
                p = 1
                for y in range(N):
                    p *= data[x + y*N + z*N*N]
                if p != product:
                    semimagic = False
                    break
        for y in range(N):
            if not semimagic:
                break;
            for z in range(N):
                p = 1
                for x in range(N):
                    p *= data[x + y*N + z*N*N]
                if p != product:
                    semimagic = False
                    break
        p = 1
        for i in range(N):
            p *= data[i + i*N + i*N*N]
        if p != product:
            diag = False
        p = 1
        for i in range(N):
            p *= data[i + i*N + (N-1-i)*N*N]
        if p != product:
            diag = False
        p = 1
        for i in range(N):
            p *= data[i + (N-1-i)*N + i*N*N]
        if p != product:
            diag = False
        p = 1
        for i in range(N):
            p *= data[i + (N-1-i)*N + (N-1-i)*N*N]
        if p != product:
            diag = False
        if semimagic or diag:
            label = f"P"
            if not diag:
                label += "(semimagic)"
            print(f"{label}={product}")

except FileNotFoundError:
    print(f"Error: The file '{fname}' was not found.")

