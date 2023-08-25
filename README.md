
# ★piler

The ★piler is a compilation infrastructure designed for creating transpilers using small transpilation functions referred to as deltas. The ★piler autonomously searches for a sequence of delta applications that result in a complete source-to-source transpilation. The process commences with an initial source program, written in a specific language (let's say language L). The system employs a specially crafted heuristic function on the delta-induced graph (which operates within a metric space) to explore and identify a transpilation meeting certain criteria. Specifically, this involves transpiling to a target language L'.

### Dependencies
The file ```requirements.txt``` enumerates the necessary Python packages. You can effortlessly install all the dependencies using ```pip3 install -r requirements.txt```. However, we recommend utilizing a virtual environment: ```python3 -m venv venv; source venv/bin/activate; python3 -m pip install -r requirements```.

### Replication
The ```src``` directory holds the source code, while the ```data``` directory contains the output from various experiments. The ```makefile``` file provides instructions for reproducing these experiments. To execute all experiments, simply run ```make figs```. If you encounter any issues at this stage, you can attempt running ```PYTHONPATH=$PYTHONPATH:. make figs``` instead. Note that the run of the full suite may require several hours. You can find the file containing all the result as ```data/benchmark.csv```.
