# Approcci di soluzione al problema di batch scheduling

### Descrizione
Il problema di batch scheduling ha l'obiettivo di minimizzare il massimo tempo di completamento di un insieme di job, caratterizzati da uno specifico tempo di 
lavorazione p<sub>j</sub> ed una dimensione s<sub>j</sub>. I job vengono raggruppati in batch e processati simultaneamente su una macchina con capacità limitata pari a B.

Questa repository contiene l'implementazione in codice Python dei modelli di programmazione lineare misto intera (MILP<sub>1</sub>, MILP<sub>1</sub>) e degli algoritmi euristici (Greedy<sub>1</sub>, Greedy<sub>2</sub> e Knapsack) per la risoluzione del problema di batch scheduling. I modelli e gli algoritmi sono stati testati su 180 istanze diverse generate attraverso uno script Python.Le istanze utilizzate per i test e i risultati dei test si trovano rispettivamente nelle cartelle 'istanze_test' e 'output_test'.

### Istruzioni
Per testare i modelli e gli algoritmi proposti, in primo luogo è necessario generare le istanze eseguendo lo script 'write_istanze.py' ed installare la libreria Python MIP utilizzata per l'implementazione dei modelli.
Successivamente, va modificato il file eseguibile 'test.bat' inserendo i percorsi degli script Python salvati all'interno del proprio dispositivo. Eseguendo poi questo file, verranno effettuati i test dei modelli e degli algoritmi su tutte le istanze generate.
I risultati dei test verranno salvati in degli apposti file .txt, che è possibile poi trasferire in dei file .csv eseguendo lo script 'write_files_csv.py'.
