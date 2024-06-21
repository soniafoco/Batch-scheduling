from mip import Model, xsum, minimize, BINARY, OptimizationStatus
from operator import itemgetter
import sys, time

# Definizione dei possibili valori di stato mostrati da Gurobi
all_status = {
    OptimizationStatus.ERROR: "ERROR",
    OptimizationStatus.OPTIMAL: "OPTIMAL",
    OptimizationStatus.INFEASIBLE: "INFEASIBLE",
    OptimizationStatus.UNBOUNDED: "UNBOUNDED",
    OptimizationStatus.FEASIBLE: "FEASIBLE",
    OptimizationStatus.INT_INFEASIBLE: "INT_INFEASIBLE",
    OptimizationStatus.NO_SOLUTION_FOUND: "NO_SOLUTION_FOUND",
    OptimizationStatus.LOADED: "LOADED",
    OptimizationStatus.CUTOFF: "CUTOFF"}


# Definizione del nome del file contenente l'istanza (se viene utilizzato un file eseguibile .bat per eseguire il file python corrente)
input_file = sys.argv[1]

# Lettura del file di input
try:
    file = open(input_file, "r", encoding="utf-8")
    line = file.readline()
    records = line.strip().split(";")

    # Capacità massima della macchina 
    B = int(records[0])
    # Numero di job
    n = int(records[1])
    line = file.readline()

    jobs = []
    while line != "":
        records = line.strip().split(";")
        # Tupla contente il tempo di lavorazione (p_j) e la dimensione (s_j) del job corrente 
        jobs.append( (int(records[0]), int(records[1])) )
        line = file.readline()
    file.close()

except IOError:
    print("Could not read file")

# Ordinamento dei job per tempi di lavorazione (p_j) non crescenti
jobs_sorted = sorted(jobs, key=itemgetter(0), reverse=True)

# Lista dei tempi di lavorazione di tutti i job
p = [job[0] for job in jobs_sorted]

# Lista delle dimensioni di tutti i job
s = [job[1] for job in jobs_sorted]

# Modello
m = Model("MILP2")

# Vraibili binarie x(j)(k) 
x = [[m.add_var('x({})({})'.format(j , k), var_type=BINARY) for k in range(j+1)] for j in range(n)] 

# Funzione obiettivo
m.objective = minimize(xsum(p[k]*x[k][k] for k in range(n)))

# Vincoli
for j in range(n):
    m.add_constr(xsum(x[j][k] for k in range(j+1)) == 1)

for k in range(n-1):
    m.add_constr(xsum(s[j]*x[j][k] for j in range(k+1,n)) <= (B-s[k])*x[k][k] )

for k in range(n):
    for j in range(k+1,n):
        m.add_constr(x[j][k] <= x[k][k])
        

# Ottimizzazione (con tempo massimo pari a 100 secondi)
start_time = time.time()
m.optimize(max_seconds=100)
end_time = time.time()
execution_time = end_time-start_time

# Scrittura del modello in un file .lp
m.write('MILP2.lp')

# Output 
print("\nValore della funzione obiettivo: %f" %m.objective_value)
for k in range(n):
    selected = []
    for j in range(n):
        if j>=k and x[j][k].x >= 0.99:
            selected.append(j)
    if len(selected)>0:
        print("\nJob selezionati all'interno del batch:")
        for i in selected:
            print("job con tempo di lavorazione %.2f e dimensione %.2f" %(p[i], s[i]))

# Scrittura del file di output "output_MILP2.txt" (possibile cambiare il nome del file in base alle preferenze)
output_file = open("output_MILP2.txt", "a")
sublist = input_file.split("\\")
istanza = sublist[-1]
output_file.write(f"ISTANZA: {istanza[:-4]}\tFO: {m.objective_value}\tBEST BOUND: {m.objective_bound}\tTEMPO: {execution_time}\tSTATO: {all_status[m.status]}\n")
output_file.close()


            
