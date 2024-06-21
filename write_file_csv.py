# Lista contenente i nomi dei file in cui sono stati salvati gli output dell'esecuzione di modelli e algoritmi testati sulle istanze (da modificare in caso siano stati salvati in file diversi)
list = ["output_MILP1.txt", "output_MILP2.txt", "output_greedy_1.txt", "output_greedy_2.txt", "output_knapsack.txt"]

# Lettura di ogni file di output presente nella lista
for input in list:
    try:
        # Scrittura di un file di output in formato .csv
        file = open(input, "r", encoding="utf-8")
        output = open(f"{input[:-4]}.csv", "a")
        line = file.readline()

        if len(line.strip().split("\t")) == 3:
            output.write("Istanza;Funzione obiettivo;Tempo\n")
        else:
            output.write("Istanza;Funzione obiettivo;Best bound;Tempo;Stato soluzione\n")

        while line != "":
            records = [x.split(":")[1].strip() for x in line.strip().split("\t")]

            string = ""
            for i in range(len(records)):
                if i==len(records)-1:
                    string += records[i]+"\n"
                else:
                    string += records[i]+";"

            output.write(string)

            line = file.readline()

        file.close()
        output.close()

    except IOError:
        print("Could not read file")