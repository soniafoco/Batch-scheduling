import time
import random

# Definizione dei diversi valori di capacità della macchina (B) e degli intervalli in cui verranno definiti i valori delle dimensioni (range_size) 
# e dei tempi di lavorazioni (range_process_time) che definiscono le 12 classi di istanze da generare
B = [10, 30, 40, 100, 100, 300, 10, 10, 10, 10, 10, 10]
range_size = [(1,10),(1,10),(1,35),(1,35),(1,100),(1,100),(1,5),(2,4),(3,7),(2,4),(1,5),(3,7)]
range_process_time = [(1,10),(1,10),(1,35),(1,35),(1,100),(1,100),(1,5),(2,4),(3,7),(1,10),(1,10),(1,10)]

# Definizione dei valori di n (numero di job) per generare le istanze
values_n = [20, 40, 60, 80, 100]

# Generazione delle istanze
for i in range(len(B)): 
    for n in values_n:
        random.seed(time.time())
        # Vengono generate 3 istanze per ogni classe e valore di n
        for j in range(3):
            # Scrittura del file contenente l'istanza all'interno della cartella "istanze"
            file = open(f"istanze/B{i+1}n{n}_{j+1}.txt", "w") 
            file.write(f"{B[i]};{n}\n") 
            for k in range(n): 
                size = random.randint(range_size[i][0], range_size[i][1])
                process_time = random.randint(range_process_time[i][0], range_process_time[i][1])
                file.write(f"{process_time};{size}\n")
            file.close()
