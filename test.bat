@echo off

REM Impostazione del percorso della cartella contenente le istanze (da modificare in base al percorso della cartella in cui si trovano le istanze)
set INSTANCES_FOLDER="..\istanze"

REM Impostazione dei percorsi degli script Python (da modificare in base al percorso di ogni script)
set PYTHON_SCRIPT1="..\MILP1.py"
set PYTHON_SCRIPT2="..\MILP2.py"
set PYTHON_SCRIPT3="..\greedy_1.py"
set PYTHON_SCRIPT4="..\greedy_2.py"
set PYTHON_SCRIPT5="..\knapsack.py"

set SCRIPTS=%PYTHON_SCRIPT1% %PYTHON_SCRIPT2% %PYTHON_SCRIPT3% %PYTHON_SCRIPT4% %PYTHON_SCRIPT5%

REM Esecuzione degli script sulle istanze 
for %%s in (%SCRIPTS%) do (
    for %%f in (%INSTANCES_FOLDER%\*.txt) do (
        python %%s "%%f"
    )
)

pause

