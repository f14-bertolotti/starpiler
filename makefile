
data/big.pickle: src/garden/language_garden.py
	python3 src/garden/language_garden.py \
		--configuration src/garden/configuration.json \
		--garden.input_path src/garden/Point.ss \
		--garden.output_path "data/big.pickle" \
		--garden.solutionset "spplang" \
		--garden.ssharp2spp True \
		--garden.spp2s True \
		--garden.s2spp False

data/small.pickle: src/garden/language_garden.py
	python3 src/garden/language_garden.py \
		--configuration src/garden/configuration.json \
		--garden.input_path src/garden/Point.ss \
		--garden.output_path "data/small.pickle" \
		--garden.solutionset "spplang" \
		--garden.ssharp2spp True \
		--garden.spp2s False \
		--garden.s2spp False

data/big-shortestpath.pdf: makefile data/big.pickle src/garden/draw_shortest_path.py
	python3 src/garden/draw_shortest_path.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/big.pickle \
		--draw.output_path data/big-shortestpath.pdf \
		--draw.width 0.1 \
		--draw.linewidth 0.1 \
		--draw.node_size 0.5 \
		--draw.show False

data/small-shortestpath.pdf: makefile data/small.pickle src/garden/draw_shortest_path.py
	python3 src/garden/draw_shortest_path.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/small.pickle \
		--draw.output_path data/small-shortestpath.pdf \
		--draw.show False

data/big-colored.pdf: makefile data/big.pickle src/garden/draw_solution_distance.py
	python3 src/garden/draw_solution_distance.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/big.pickle \
		--draw.output_path data/big-colored.pdf \
		--draw.width 0.1 \
		--draw.linewidth 0.1 \
		--draw.node_size 0.5 \
		--draw.show False

data/small-colored.pdf: makefile data/small.pickle src/garden/draw_solution_distance.py
	python3 src/garden/draw_solution_distance.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/small.pickle \
		--draw.output_path data/small-colored.pdf \
		--draw.show False

data/big-bfs.pdf: makefile data/big.pickle src/garden/draw_BFS.py
	python3 src/garden/draw_BFS.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/big.pickle \
		--draw.output_path data/big-bfs.pdf \
		--draw.width 0.1 \
		--draw.linewidth 0.1 \
		--draw.node_size 0.5 \
		--draw.show False

data/small-bfs.pdf: makefile data/small.pickle src/garden/draw_BFS.py
	python3 src/garden/draw_BFS.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/small.pickle \
		--draw.output_path data/small-bfs.pdf \
		--draw.show False

data/big-astar.pdf: makefile data/big.pickle src/garden/draw_Astar.py
	python3 src/garden/draw_Astar.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/big.pickle \
		--draw.output_path data/big-astar.pdf \
		--draw.width 0.1 \
		--draw.linewidth 0.1 \
		--draw.node_size 0.5 \
		--draw.show False

data/small-astar.pdf: makefile data/small.pickle src/garden/draw_Astar.py
	python3 src/garden/draw_Astar.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/small.pickle \
		--draw.output_path data/small-astar.pdf \
		--draw.show False

figs: data/small-astar.pdf \
	  data/small-bfs.pdf \
	  data/small-colored.pdf \
	  data/small-shortestpath.pdf \
	  data/big-astar.pdf \
	  data/big-bfs.pdf data/ \
	  data/big-colored.pdf \
	  data/big-shortestpath.pdf


clean: 
	rm data/*
