import numpy as np
import random as rd
import sys
import datetime

N = 2
tau = 0
count = 10000

def sign(a): 
    if a <= 0: return -1
    return 1

def decision_stump(d:list):
    d.sort()
    d_sort = d

    theta = []
    theta.append(-1)
    for i in range(N-1):
        tmp = (d_sort[i] + d_sort[i + 1])/2
        theta.append(tmp)

    E_in_list = []
    for th in theta:
        for s in [-1, 1]:
            E_in_list_element = []
            E_in_list_element.append(th)
            E_in_list_element.append(s)
            E_in = 0
            for d in d_sort:
                err = sign(s * (d - th)) != sign(d)
                if rd.random() < tau: err = not err
                if err: 
                    E_in += 1/N
            E_in_list_element.append(E_in)
            E_in_list.append(E_in_list_element)
    
    min_E_in = 1
    min = [0, 0, 0]
    for e in range(len(E_in_list)):
        if E_in_list[e][2] < min_E_in:
            min_E_in = E_in_list[e][2]
            min[0] = (E_in_list[e][0])
            min[1] = (E_in_list[e][1])
            min[2] = (E_in_list[e][2])
            # print(time, "\t", min)
        elif (E_in_list[e][2] == min_E_in) and ((E_in_list[e][0] + E_in_list[e][1]) < (min[0] + min[1])) :
            min_E_in = E_in_list[e][2]
            min = []
            min.append(E_in_list[e][0])
            min.append(E_in_list[e][1])
            min.append(E_in_list[e][2])
    return min


ans = 0
ans_a = 0
time = 0
for iteration in range(count):
    dataSet = []
    for i in range(N):
        dataSet.append(rd.random() * 2 - 1)
    result = []
    result = decision_stump(dataSet)
    E_out = (1.0 - tau) * 0.5 * abs(float(result[0])) + tau * (1.0 - 0.5 * abs(float(result[0])))
    ans += (E_out - result[2])
    ans_a += abs(E_out - result[2])
    time += 1
ans /= count
ans_a /= count
print("16. E_out(g, 0) - E_in(g) = ", ans)
print("16. |E_out(g, 0) - E_in(g)| = ", ans_a)
print("\n")

N = 20
ans = 0
ans_a = 0
time = 0
for iteration in range(count):
    dataSet = []
    for i in range(N):
        dataSet.append(rd.random() * 2 - 1)
    result = []
    result = decision_stump(dataSet)
    E_out = (1.0 - tau) * 0.5 * abs(float(result[0])) + tau * (1.0 - 0.5 * abs(float(result[0])))
    ans += (E_out - result[2])
    ans_a += abs(E_out - result[2])
    time += 1
ans /= count
ans_a /= count
print("17. E_out(g, 0) - E_in(g)", ans)
print("17. |E_out(g, 0) - E_in(g)| = ", ans_a)
print("\n")

N = 2
tau = 0.1
ans = 0
ans_a = 0
time = 0
for iteration in range(count):
    dataSet = []
    for i in range(N):
        dataSet.append(rd.random() * 2 - 1)
    result = []
    result = decision_stump(dataSet)
    E_out = (1.0 - tau) * 0.5 * abs(float(result[0])) + tau * (1.0 - 0.5 * abs(float(result[0])))
    ans += (E_out - result[2])
    ans_a += abs(E_out - result[2])
    time += 1
ans /= count
ans_a /= count
print("18. E_out(g, 0.1) - E_in(g)", ans)
print("18. |E_out(g, 0.1) - E_in(g)| = ", ans_a)
print("\n")

N = 20
tau = 0.1
ans = 0
ans_a = 0
time = 0
for iteration in range(count):
    dataSet = []
    for i in range(N):
        dataSet.append(rd.random() * 2 - 1)
    result = []
    result = decision_stump(dataSet)
    E_out = (1.0 - tau) * 0.5 * abs(float(result[0])) + tau * (1.0 - 0.5 * abs(float(result[0])))
    ans += (E_out - result[2])
    ans_a += abs(E_out - result[2])
    time += 1
ans /= count
ans_a /= count
print("19. E_out(g, 0.1) - E_in(g)", ans)
print("19. |E_out(g, 0.1) - E_in(g)| = ", ans_a)
print("\n")

N = 200
tau = 0.1
ans = 0
ans_a = 0
time = 0
for iteration in range(count):
    dataSet = []
    for i in range(N):
        dataSet.append(rd.random() * 2 - 1)
    result = []
    result = decision_stump(dataSet)
    E_out = (1.0 - tau) * 0.5 * abs(float(result[0])) + tau * (1.0 - 0.5 * abs(float(result[0])))
    ans += (E_out - result[2])
    ans_a += abs(E_out - result[2])
    time += 1
ans /= count
ans_a /= count
print("20. E_out(g, 0.1) - E_in(g)", ans)
print("20. |E_out(g, 0.1) - E_in(g)| = ", ans_a)
print("\n")