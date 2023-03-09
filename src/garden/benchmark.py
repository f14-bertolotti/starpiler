
import gc, tqdm, pandas, pathlib, configator, tracemalloc

from src.syntax          import slang, spplang, ssharplang
from src.transpilers     import MetaTranspiler
from src.transpilers     import deltas, ssharp2spp_deltas, spp2s_deltas, s2spp_deltas
from src.transpilers.spp import metric01 as spp_metric
from src.transpilers.s   import metric01 as s_metric
from src.testing         import ssharp_tests, spp_tests, s_tests
from src.utils           import lang2rules

s_rules, spp_rules, ssharp_rules = lang2rules(slang), lang2rules(spplang), lang2rules(ssharplang)
configuration = configator.Configator()

excluded = {"point", "struct_class3", "struct_class2", "struct_class", "variable_declaration2", "sizeof_struct"}

data = pandas.DataFrame(columns=["name", "path", "search", "sourcelang", "targetlang", "visited"] + 
                                [f"time{i}(s)"   for i in range(configuration.benchmark.trials)] + 
                                [f"memory{i}(KB)" for i in range(configuration.benchmark.trials)])

def trace_memory(f):
    gc.collect()
    tracemalloc.start()
    tracemalloc.clear_traces()
    f()
    _,peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak/(1024)

def trace_time(f):
    gc.collect()
    import time
    start = time.time()
    f()
    end = time.time()
    return end-start

def add_row(dataframe, lang, sourcelangname, targetlangname, path, deltas, metric, rules):
    source_tree = lang.parse(pathlib.Path(path).read_text())
    BFSTimes   = [trace_time(lambda:MetaTranspiler(deltas, metric).search      (source_tree))        for _ in range(configuration.benchmark.trials)]
    AstarTimes = [trace_time(lambda:MetaTranspiler(deltas, None  ).search_Astar(source_tree, rules)) for _ in range(configuration.benchmark.trials)]
    BFSMems    = [trace_memory(lambda:MetaTranspiler(deltas, metric).search      (source_tree))        for _ in range(configuration.benchmark.trials)]
    AstarMems  = [trace_memory(lambda:MetaTranspiler(deltas, None  ).search_Astar(source_tree, rules)) for _ in range(configuration.benchmark.trials)]
    BFSvisited   = len(MetaTranspiler(deltas, metric, return_visited=True).search(source_tree)[1])
    Astarvisited = len(MetaTranspiler(deltas,   None, return_visited=True).search_Astar(source_tree, rules)[1])
    dataframe.loc[dataframe.shape[0]] = [name, path, "BFS", sourcelangname, targetlangname, BFSvisited  , *BFSTimes  , *BFSMems]
    print(dataframe.loc[dataframe.shape[0]-1])
    dataframe.loc[dataframe.shape[0]] = [name, path, "A*" , sourcelangname, targetlangname, Astarvisited, *AstarTimes, *AstarMems]
    print(dataframe.loc[dataframe.shape[0]-1])

if configuration.benchmark.s2spp:
    for name, test in tqdm.tqdm(list(filter(lambda x:x[0] not in excluded, s_tests.items())), desc="S->S++"):
        add_row(data, slang, "S", "S++", test["path"], s2spp_deltas, spp_metric, spp_rules)

if configuration.benchmark.spp2s:
    for name, test, in tqdm.tqdm(spp_tests.items(), desc="S++->S"):
        add_row(data, spplang, "S++", "S", test["path"], spp2s_deltas, s_metric, s_rules)

if configuration.benchmark.ssharp2spp:
    for name, test, in tqdm.tqdm(ssharp_tests.items(), desc="S#->S++"):
        add_row(data, ssharplang, "S#", "S++", test["path"], ssharp2spp_deltas, spp_metric, spp_rules)

data.to_csv(configuration.benchmark.output_path)






