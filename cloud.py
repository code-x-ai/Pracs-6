from tabulate import tabulate

vms = [
    {"name": "VM1", "mips": 500},
    {"name": "VM2", "mips": 1000},
    {"name": "VM3", "mips": 1500},
]
tasks = [
    {"name": "Task1", "length": 80000},
    {"name": "Task2", "length": 15000},
    {"name": "Task3", "length": 15000},
    {"name": "Task4", "length": 80000},
    {"name": "Task5", "length": 15000},
]

def round_robin():
    load = [0]*3; res = []
    for i, t in enumerate(tasks):
        j = i % 3
        st = load[j] / vms[j]["mips"]
        et = t["length"] / vms[j]["mips"]
        res.append([t["name"], vms[j]["name"], round(st,2), round(et,2), round(st+et,2)])
        load[j] += t["length"]
    return res

def least_loaded():
    load = [0]*3; res = []
    for t in tasks:
        j = min(range(3), key=lambda i: load[i] / vms[i]["mips"])
        st = load[j] / vms[j]["mips"]
        et = t["length"] / vms[j]["mips"]
        res.append([t["name"], vms[j]["name"], round(st,2), round(et,2), round(st+et,2)])
        load[j] += t["length"]
    return res

h = ["Task", "VM", "Start Time", "Execution Time", "Finish Time"]
r1, r2 = round_robin(), least_loaded()
print("\nRound Robin Scheduling\n")
print(tabulate(r1, headers=h, tablefmt="grid"))
print("\nLeast-Loaded Scheduling\n")
print(tabulate(r2, headers=h, tablefmt="grid"))
m1 = max(r[4] for r in r1); m2 = max(r[4] for r in r2)
print("\nScheduling Performance Comparison\n")
print(tabulate([["Round Robin", m1], ["Least-Loaded", m2]],
               headers=["Scheduling Method", "Total Completion Time"], tablefmt="grid"))
print(f"\nPerformance Improvement: {(m1-m2)/m1*100:.2f}%")
