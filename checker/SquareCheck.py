#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SquareCheck.py: Magic Square Analyzer

Verification Suite:
1. Duplicate/Sequence Check: Validates if elements are unique and form a continuous sequence (starting from 0 or 1).
2. Power Sums (S_k): Checks if the sum of x_i^k is constant for k = 1 to 7.
3. Product (P): Checks if the product of x_i is constant.
4. Mult1 (P1): Checks if the product of x_i^x_i is constant.

Output:
- Displays the constant value only for conditions that are satisfied across all lines.

License: CC BY 4.0
Copyright (c) 2025 Toshihiro Shirakawa
"""

import math
import sys
sys.set_int_max_str_digits(0)

MAX_POWER = 7

def check_regularity(data, n):
    unique = set(data)
    if len(unique) != n * n:
        print(f"Error: Duplicate elements found! (Unique: {len(unique)})")
        return

    min_val = min(unique)
    max_val = max(unique)

    if min_val == 0 and max_val == n * n - 1:
        print(f"Normal (0 to {max_val})")
    elif min_val == 1 and max_val == n * n:
        print(f"Normal (1 to {max_val})")
    else:
        print(f"Non-normal (Range: {min_val} to {max_val})")

def factors_update(factorcount, num):
    x = num
    while x % 2 == 0:
        if len(factorcount) <= 2:
            factorcount.extend([0] * (2 + 1 - len(factorcount)))
        factorcount[2] += num
        x //= 2
    p = 3
    while p * p <= x:
        while x % p == 0:
            if len(factorcount) <= p:
                factorcount.extend([0] * (p + 1 - len(factorcount)))
            factorcount[p] += num
            x //= p
        p += 2
    if x > 1:
        if len(factorcount) <= x:
            factorcount.extend([0] * (x + 1 - len(factorcount)))
        factorcount[x] += num
    return factorcount

fname = input("Input Magic Square file name: ")

try:
    data = []
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

    N = math.isqrt(len(data))
    if N * N != len(data):
        print(f"Error: {len(data)} is not square")
    else:
        print(f"{N}*{N} Square")
        check_regularity(data, N)
        for k in range(1,MAX_POWER + 1):
            semimagic = True
            diag = True
            sum = 0
            for i in range(N):
                sum += data[i] ** k
            for i in range(N):
                s = 0
                for j in range(N):
                    s += data[i*N+j] ** k
                if s != sum:
                    semimagic = False
                    break
            if semimagic:
                for i in range(N):
                    s = 0
                    for j in range(N):
                        s += data[i+j*N] ** k
                    if s != sum:
                        semimagic = False
                        break
            s = 0
            for i in range(N):
                s += data[i+i*N] ** k
            if s != sum:
                diag = False
            s = 0
            for i in range(N):
                s += data[N-1-i+i*N] ** k
            if s != sum:
                diag = False
            if semimagic or diag:
                label = f"S{k}"
                if not diag:
                    label += "(semimagic)"
                print(f"{label}={sum}")

        semimagic = True
        diag = True
        product = 1
        for i in range(N):
            product *= data[i]
        for i in range(N):
            p = 1
            for j in range(N):
                p *= data[i*N+j]
            if p != product:
                semimagic = False
                break
        if semimagic:
            for i in range(N):
                p = 1
                for j in range(N):
                    p *= data[i+j*N]
                if p != product:
                    semimagic = False
                    break
        p = 1
        for i in range(N):
            p *= data[i+i*N]
        if p != product:
            diag = False
        p = 1
        for i in range(N):
            p *= data[N-1-i+i*N]
        if p != product:
            diag = False
        if semimagic or diag:
            label = f"P"
            if not diag:
                label += "(semimagic)"
            print(f"{label}={product}")
        if semimagic:
            semimagic = True
            diag = True
            product = 1
            basefactors = []
            for i in range(N):
                basefactors = factors_update(basefactors, data[i])
            for i in range(N):
                factors = []
                for j in range(N):
                    factors =  factors_update(factors, data[i*N+j])
                if factors != basefactors:
                    semimagic = False
                    break
            if semimagic:
                for i in range(N):
                    factors = []
                    for j in range(N):
                        factors =  factors_update(factors, data[i+j*N])
                    if factors != basefactors:
                        semimagic = False
                        break
            factors = []
            for i in range(N):
                factors =  factors_update(factors, data[i+i*N])
            if factors != basefactors:
                diag = False
            factors = []
            for i in range(N):
                factors =  factors_update(factors, data[N-1-i+i*N])
            if factors != basefactors:
                diag = False
            if semimagic or diag:
                label = f"P1"
                if not diag:
                    label += "(semimagic)"
                print(f"{label}=", end="")
                for i in range(len(basefactors)):
                    if(basefactors[i] > 0):
                        print(f"{i}^{basefactors[i]}.", end="")
except FileNotFoundError:
    print(f"Error: The file '{fname}' was not found.")

