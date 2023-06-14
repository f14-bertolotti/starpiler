import configator, seaborn, pandas
import matplotlib.pyplot as plt

configuration = configator.Configator()

data = pandas.read_csv(configuration.benchmark.input_path)
data = data.loc[data["sourcelang"]==configuration.benchmark.draw.sourcelang].loc[data["targetlang"]==configuration.benchmark.draw.targetlang]

data["time"] = data[["time0(s)","time1(s)","time2(s)","time3(s)","time4(s)"]].mean(axis=1)

data.loc["BFS avg."] = data.loc[data["search"]=="BFS"].mean(numeric_only=True)
data.loc["BFS avg.", "search"] = "BFS"
data.loc["BFS avg.", "name"] = "avg."
data.loc["BFS avg.", "sourcelang"] = configuration.benchmark.draw.sourcelang
data.loc["BFS avg.", "targetlang"] = configuration.benchmark.draw.targetlang
data.loc["A* avg."] = data.loc[data["search"]=="A*"].mean(numeric_only=True)
data.loc["A* avg.", "search"] = "A*"
data.loc["A* avg.", "name"] = "avg."
data.loc["A* avg.", "sourcelang"] = configuration.benchmark.draw.sourcelang
data.loc["A* avg.", "targetlang"] = configuration.benchmark.draw.targetlang

fig = plt.figure(
    figsize=(configuration.benchmark.draw.sizex,configuration.benchmark.draw.sizey), 
    dpi=configuration.benchmark.draw.dpi, 
    layout="tight")

ax = seaborn.barplot(
                     data=data, 
                     x=configuration.benchmark.draw.x, 
                     y=configuration.benchmark.draw.y,
                     hue=configuration.benchmark.draw.hue,
                     log=configuration.benchmark.draw.log)

ax.set_ylabel("")
ax.set_xlabel(configuration.benchmark.draw.label)
ax.spines[['right', 'top']].set_visible(False)
ax.set_yticklabels([f"test {i:02d}" if "avg" not in x.get_text() else "average" for i,x in enumerate(ax.get_yticklabels())])

fig.savefig(configuration.benchmark.draw.output_path,
            format=configuration.benchmark.draw.format,
            transparent=True)

def replace_sharp(s):
    return s.replace("#","\\#")

def filename(search, srclang, tgtlang):
    if srclang == "S#": srclang = "ssharp"
    elif srclang == "S++": srclang = "splusplus"
    elif srclang == "S": srclang = "s"
    else: assert False
    if tgtlang == "S#": tgtlang = "ssharp"
    elif tgtlang == "S++": tgtlang = "splusplus"
    elif tgtlang == "S": tgtlang = "s"
    else: assert False
    return f"{search}-{srclang}-{tgtlang}.tex"

#### BFS to latex ####
table = data.loc[data["search"]=="BFS"][["visited","time","time0(s)","time1(s)","time2(s)","time3(s)","time4(s)"]].copy()
table["index"] = [f"{i:02d}" if i != len(table)-1 else "avg." for i in range(0, len(table))]
table["visited"] = table["visited"].astype(int)
table = table[["index","visited","time","time0(s)","time1(s)","time2(s)","time3(s)","time4(s)"]]

table.to_latex(
    configuration.benchmark.draw.latex_path + filename("BFS",configuration.benchmark.draw.sourcelang,configuration.benchmark.draw.targetlang), 
    index=False,
    longtable=True,
    header=["test","visited","avg. time","trial 0","trial 1","trial 2", "trial 3", "trial 4"],
    caption=f"Number of node visited and trials times (in seconds) for the BFS algorithm when translating {replace_sharp(configuration.benchmark.draw.sourcelang)} to {replace_sharp(configuration.benchmark.draw.targetlang)}.",
    label="table:"+filename("BFS",configuration.benchmark.draw.sourcelang,configuration.benchmark.draw.targetlang)
)

#### A* to latex ####
table = data.loc[data["search"]=="A*"][["visited","time","time0(s)","time1(s)","time2(s)","time3(s)","time4(s)"]].copy()
table["index"] = [f"{i:02d}" if i != len(table)-1 else "avg." for i in range(0, len(table))]
table["visited"] = table["visited"].astype(int)
table = table[["index","visited","time","time0(s)","time1(s)","time2(s)","time3(s)","time4(s)"]]

table.to_latex(
    configuration.benchmark.draw.latex_path + filename("Astar",configuration.benchmark.draw.sourcelang,configuration.benchmark.draw.targetlang), 
    index=False,
    longtable=True,
    header=["test","visited","avg. time","trial 0","trial 1","trial 2", "trial 3", "trial 4"],
    caption="Number of node visited and trials times (in seconds) for the A\\textsuperscript{*} algorithm when translating "+f"{replace_sharp(configuration.benchmark.draw.sourcelang)} to {replace_sharp(configuration.benchmark.draw.targetlang)}.",
    label="table:"+filename("Astar",configuration.benchmark.draw.sourcelang,configuration.benchmark.draw.targetlang)
)
