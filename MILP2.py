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
            B = int(records[1])
        elif records[0]=="J":
            # Processing time of job
            p.append(int(records[1]))
            # Size of job
            s.append(int(records[2]))
        line = file.readline()
    file.close()
except IOError:
    print("Could not read file")

# Sorting processing times in descending order
p.sort(reverse=True)

# Number of jobs
n = len(s)

# Model
m = Model("MILP2")

# Binary variables x(k)(k)
x = [[m.add_var('x({})({})'.format(j , k), var_type=BINARY) for j in range(n)] for k in range(n)] 

# Objective function
m.objective = minimize(xsum(p[k]*x[k][k] for k in range(n)))

# Constrains
for j in range(n):
    m.add_constr(xsum(x[j][k] for k in range(j+1)) == 1)

for k in range(n-1):
    m.add_constr(xsum(s[j]*x[j][k] for j in range(k+1,n)) <= (B-s[k])*x[k][k] )

for j in range(n):
    for k in range(n):
        m.add_constr(x[j][k] <= x[k][k])

# Optimization
m.optimize()

# Writing model
m.write('MILP2.lp')

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