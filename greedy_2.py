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
        # Tupla contente il tempo di lavorazione (p_j), la dimensione (s_j) e il valore di p_j/s_j del job corrente
        jobs.append( (int(records[0]), int(records[1]), int(records[0])/int(records[1]) ) )
        line = file.readline()
    file.close()

except IOError:
    print("Could not read file")

# Ordinamento dei job per valori di p_j/s_j non crescenti
jobs_sorted = sorted(jobs, key=itemgetter(2), reverse=True)

# Algoritmo 
start_time = time.time()
objective_function = 0
solution = []
p = []
s = []
batch = []
while len(jobs_sorted) > 0:
    for i in range(len(jobs_sorted)):
        if sum(s)+jobs_sorted[i][1] <= B:
            p.append(jobs_sorted[i][0])
            s.append(jobs_sorted[i][1])
            batch.append(jobs_sorted[i])
    for job in batch:
        jobs_sorted.remove(job)
    solution.append(batch)
    objective_function += max(p)
    p = []
    s = []
    batch = []

end_time = time.time()
execution_time = end_time-start_time

# Output
print("\nValore della funzione obiettivo: %f" %objective_function)
for batch in solution:
    print("\nJob selezionati all'interno del batch:")
    for job in batch:
        print("job con tempo di lavorazione %.2f e dimensione %.2f" %(job[0], job[1]))

# Scrittura del file di output "output_greedy_2.txt" (possibile cambiare il nome del file in base alle preferenze)
output_file = open("output_greedy_2.txt", "a")
sublist = input_file.split("\\")
istanza = sublist[-1]
output_file.write(f"ISTANZA: {istanza[:-4]}\tFO: {objective_function}\tTEMPO: {execution_time}\n")
output_file.close()
