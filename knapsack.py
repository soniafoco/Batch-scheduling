from mip import Model, xsum, maximize, BINARY
from operator import itemgetter
import sys, time

# Definizione del nome del file contenente l'istanza (se viene utilizzato un file eseguibile .bat per eseguire il file python corrente)
input_file = sys.argv[1]

jobs = []

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

    while line != "":
        records = line.strip().split(";")
        # Tupla contente il tempo di lavorazione (p_j) e la dimensione (s_j) del job corrente
        jobs.append( (int(records[0]), int(records[1])) )
        line = file.readline()
    file.close()

except IOError:
    print("Could not read file")


# Lista dei tempi di lavorazione di tutti i job
p = [job[0] for job in jobs]

# Lista delle dimensioni di tutti i job
s = [job[1] for job in jobs]

# Algoritmo 
start_time = time.time()
makespan = 0
i = 0
while len(jobs)>0: 
    # Risoluzione Knapsack Problem utilizzando il solver Gurobi
    # Modello
    m = Model(f"euristica2_{i}")

    # Variabili binarie x(j)(k) 
    x = [m.add_var('x({})'.format(j), var_type=BINARY) for j in range(len(jobs))] 

    # Funzione obiettivo
    m.objective = maximize(xsum(jobs[j][0]*x[j] for j in range(len(jobs))))

    # Vincolo
    m.add_constr(xsum(jobs[j][1]*x[j] for j in range(len(jobs))) <= B)

    # Ottimizzazione
    m.optimize()

    # Output del batch corrente
    max_process_time = 0
    print("Job selezionati all'interno del batch::")
    selected = []
    for j in range(len(jobs)):
        print(x[j])
        if x[j].x >= 0.99:
            selected.append(jobs[j])
            print(jobs[j])
    for job in selected:
        print("job con tempo di lavorazione %.2f e dimensione %.2f" %(job[0], job[1]))
        if job[0]>max_process_time:
            max_process_time = job[0]
        jobs.remove(job)

    makespan += max_process_time
    i += 1

end_time = time.time()
execution_time = end_time-start_time

print("\nValore della funzione obiettivo %f" %m.makespan)

#Output file "output_knapsack.txt"
output_file = open("output_knapsack.txt", "a")
sublist = input_file.split("\\")
istanza = sublist[-1]
output_file.write(f"ISTANZA: {istanza[:-4]}\tFO: {makespan}\tTEMPO: {execution_time}\n")
output_file.close()
            
#3 istanze diverse (random) per ogni classe e per ogni n = {20,40,60,80,100}   12*5=60*3=180 istanze
#100/60 secondi 
#optimize(max_seconds=)

# nome file (istanza) --> valore FO --> tempo --> best bound --> stato soluzione