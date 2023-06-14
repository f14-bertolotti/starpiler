
data/big.pickle: src/garden/language_garden.py
	python3 src/garden/language_garden.py \
		--configuration src/garden/configuration.json \
		--garden.input_path src/garden/Point.ss \
		--garden.output_path "data/big.pickle" \
		--garden.solutionset "spplang" \
		--garden.ssharp2spp 1.0 \
		--garden.spp2s 0.4 \
		--garden.s2spp 0.0 \
		--garden.seed 1 

data/small.pickle: src/garden/language_garden.py
	python3 src/garden/language_garden.py \
		--configuration src/garden/configuration.json \
		--garden.input_path src/garden/Point.ss \
		--garden.output_path "data/small.pickle" \
		--garden.solutionset "spplang" \
		--garden.ssharp2spp 1.0 \
		--garden.spp2s 0.0 \
		--garden.s2spp 0.0 \
		--garden.seed 2 

data/big-shortestpath.pdf: data/big.pickle src/garden/draw_shortest_path.py
	python3 src/garden/draw_shortest_path.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/big.pickle \
		--draw.output_path data/big-shortestpath.pdf \
		--draw.width 0.1 \
		--draw.linewidth 0.1 \
		--draw.node_size 0.5 \
		--draw.show False

data/small-shortestpath.pdf: data/small.pickle src/garden/draw_shortest_path.py
	python3 src/garden/draw_shortest_path.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/small.pickle \
		--draw.output_path data/small-shortestpath.pdf \
		--draw.rgba_visited.a 0.2 \
		--draw.show False

data/big-colored.pdf: data/big.pickle src/garden/draw_solution_distance.py
	python3 src/garden/draw_solution_distance.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/big.pickle \
		--draw.output_path data/big-colored.pdf \
		--draw.width 0.1 \
		--draw.linewidth 0.1 \
		--draw.node_size 0.5 \
		--draw.show False

data/small-colored.pdf: data/small.pickle src/garden/draw_solution_distance.py
	python3 src/garden/draw_solution_distance.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/small.pickle \
		--draw.output_path data/small-colored.pdf \
		--draw.rgba_visited.a 0.2 \
		--draw.show False

data/big-bfs.pdf: data/big.pickle src/garden/draw_BFS.py
	python3 src/garden/draw_BFS.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/big.pickle \
		--draw.output_path data/big-bfs.pdf \
		--draw.width 0.1 \
		--draw.linewidth 0.1 \
		--draw.node_size 0.5 \
		--draw.show False

data/small-bfs.pdf: data/small.pickle src/garden/draw_BFS.py
	python3 src/garden/draw_BFS.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/small.pickle \
		--draw.output_path data/small-bfs.pdf \
		--draw.rgba_visited.a 0.2 \
		--draw.show False

data/big-astar.pdf: data/big.pickle src/garden/draw_Astar.py
	python3 src/garden/draw_Astar.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/big.pickle \
		--draw.output_path data/big-astar.pdf \
		--draw.width 0.1 \
		--draw.linewidth 0.1 \
		--draw.node_size 0.5 \
		--draw.show False

data/small-astar.pdf: data/small.pickle src/garden/draw_Astar.py
	python3 src/garden/draw_Astar.py \
		--configuration src/garden/configuration.json \
		--draw.input_path data/small.pickle \
		--draw.output_path data/small-astar.pdf \
		--draw.rgba_visited.a 0.2 \
		--draw.show False

data/rsdd3d.pdf: src/garden/draw_rsdd3D.py
	python3 src/garden/draw_rsdd3D.py \
		--configuration src/garden/configuration.json \
		--rsdd3D.output_path data/rsdd3d.pdf \
		--rsdd3D.size 130 \
		--rsdd3D.radius 15 \
		--rsdd3D.show False

data/benchmark.csv: src/garden/benchmark.py
	mkdir -p data
	python3 src/garden/benchmark.py \
		--configuration src/garden/configuration.json \
		--benchmark.output_path data/benchmark.csv

data/spp2s_time.pdf: data/benchmark.csv src/garden/draw_benchmark.py 
	python3 src/garden/draw_benchmark.py \
		--configuration src/garden/configuration.json \
		--benchmark.draw.output_path data/spp2s_time.pdf \
		--benchmark.draw.sourcelang "S++" \
		--benchmark.draw.targetlang "S" \
		--benchmark.draw.x "time" \
		--benchmark.draw.y "name" \
		--benchmark.draw.hue "search" \
		--benchmark.draw.label "time (s)" \
		--benchmark.draw.log False

data/spp2s_visited.pdf: data/benchmark.csv src/garden/draw_benchmark.py 
	python3 src/garden/draw_benchmark.py \
		--configuration src/garden/configuration.json \
		--benchmark.draw.output_path data/spp2s_visited.pdf \
		--benchmark.draw.sourcelang "S++" \
		--benchmark.draw.targetlang "S" \
		--benchmark.draw.x "visited" \
		--benchmark.draw.y "name" \
		--benchmark.draw.hue "search" \
		--benchmark.draw.label "# nodes" \
		--benchmark.draw.log False

data/ssharp2spp_time.pdf: data/benchmark.csv src/garden/draw_benchmark.py 
	python3 src/garden/draw_benchmark.py \
		--configuration src/garden/configuration.json \
		--benchmark.draw.output_path data/ssharp2spp_time.pdf \
		--benchmark.draw.sourcelang "S#" \
		--benchmark.draw.targetlang "S++" \
		--benchmark.draw.x "time" \
		--benchmark.draw.y "name" \
		--benchmark.draw.hue "search" \
		--benchmark.draw.label "time (s)" \
		--benchmark.draw.log True

data/ssharp2spp_visited.pdf: data/benchmark.csv src/garden/draw_benchmark.py 
	python3 src/garden/draw_benchmark.py \
		--configuration src/garden/configuration.json \
		--benchmark.draw.output_path data/ssharp2spp_visited.pdf \
		--benchmark.draw.sourcelang "S#" \
		--benchmark.draw.targetlang "S++" \
		--benchmark.draw.x "visited" \
		--benchmark.draw.y "name" \
		--benchmark.draw.hue "search" \
		--benchmark.draw.label "# nodes" \
		--benchmark.draw.log True

data/s2spp_time.pdf: data/benchmark.csv src/garden/draw_benchmark.py 
	python3 src/garden/draw_benchmark.py \
		--configuration src/garden/configuration.json \
		--benchmark.draw.output_path data/s2spp_time.pdf \
		--benchmark.draw.sourcelang "S" \
		--benchmark.draw.targetlang "S++" \
		--benchmark.draw.x "time" \
		--benchmark.draw.y "name" \
		--benchmark.draw.hue "search" \
		--benchmark.draw.label "time (s)" \
		--benchmark.draw.sizex 6 \
		--benchmark.draw.sizey 14 \
		--benchmark.draw.log False

data/s2spp_visited.pdf:data/benchmark.csv src/garden/draw_benchmark.py 
	python3 src/garden/draw_benchmark.py \
		--configuration src/garden/configuration.json \
		--benchmark.draw.output_path data/s2spp_visited.pdf \
		--benchmark.draw.sourcelang "S" \
		--benchmark.draw.targetlang "S++" \
		--benchmark.draw.x "visited" \
		--benchmark.draw.y "name" \
		--benchmark.draw.hue "search" \
		--benchmark.draw.label "# nodes" \
		--benchmark.draw.sizex 6 \
		--benchmark.draw.sizey 14 \
		--benchmark.draw.log False

benchmarkfigs: data/spp2s_time.pdf \
			   data/spp2s_visited.pdf \
			   data/s2spp_time.pdf \
			   data/s2spp_visited.pdf \
			   data/ssharp2spp_time.pdf \
			   data/ssharp2spp_visited.pdf \


graphfigs: data/small-astar.pdf \
	       data/small-bfs.pdf \
	       data/small-colored.pdf \
	       data/small-shortestpath.pdf \
	       data/big-astar.pdf \
	       data/big-bfs.pdf data/ \
	       data/big-colored.pdf \
	       data/big-shortestpath.pdf \
	       data/rsdd3d.pdf

figs: benchmarkfigs graphfigs


clean: 
	rm data/*
