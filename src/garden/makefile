
data/big.pickle: 
	python3 src/garden/language_garden.py \
		--configuration src/garden/configuration.json \
		--garden.input_path data/Point.ss \
		--garden.output_path "data/big.pickle" \
		--garden.solutionset "spplang" \
		--garden.ssharp2spp True \
		--garden.spp2s True \
		--garden.s2spp False

data/small.pickle: 
	python3 src/garden/language_garden.py \
		--configuration src/garden/configuration.json \
		--garden.input_path data/Point.ss \
		--garden.output_path "data/small.pickle" \
		--garden.solutionset "spplang" \
		--garden.ssharp2spp True \
		--garden.spp2s False \
		--garden.s2spp False
