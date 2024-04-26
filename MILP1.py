from mip import Model, xsum, minimize, BINARY

# Reading file
try:
    file = open("input.txt", "r", encoding="utf-8")
    line = file.readline()
    p = []
    s = []
    while line != "":
        records = line.strip().split(";")
        if records[0]=="B":
            # Batch capacity
            B = float(records[1])
        elif records[0]=="J":
            # Processing time of job
            p.append(float(records[1]))
            # Size of job
            s.append(float(records[2]))
        line = file.readline()
    file.close()
except IOError:
    print("Could not read file")

# Number of jobs
n = len(s)

# Model
m = Model("MILP1")

# Binary variables x(j)(k)
x = [[m.add_var('x({})({})'.format(j , k), var_type=BINARY) for j in range(n)] for k in range(n)]

# Continuos variables P(k)
P = [m.add_var('P({})'.format(k)) for k in range(n)]

# Objective function
m.objective = minimize(xsum(P))

# Constrains
for j in range(n):
    m.add_constr(xsum(x[j][k] for k in range(n)) == 1)

for k in range(n):
    m.add_constr(xsum(s[j]*x[j][k] for j in range(n)) <= B)

for j in range(n):
    for k in range(n):
        m.add_constr((p[j]*x[j][k]) <= P[k])

# Optimization
m.optimize()

# Writing model
m.write('MILP1.lp')

# Output 
print("\n\nOptimal solution: %f" %m.objective_value)
for k in range(n):
    selected = []
    for j in range(n):
        if x[j][k].x >= 0.99:
            selected.append(j)
    if len(selected)>0:
        print("\nSelected jobs for batch:")
        for i in selected:
            print("job %d with processing time %.2f and size %.2f" %(i+1, p[i], s[i]))



