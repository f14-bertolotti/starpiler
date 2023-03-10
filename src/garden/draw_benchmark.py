import configator, seaborn, pandas
import matplotlib.pyplot as plt

configuration = configator.Configator()

data = pandas.read_csv(configuration.benchmark.input_path)

fig = plt.figure(
    figsize=(configuration.benchmark.draw.sizex,configuration.benchmark.draw.sizey), 
    dpi=configuration.benchmark.draw.dpi, 
    layout="tight")

ax = seaborn.barplot(
                     data=data.loc[data["sourcelang"]==configuration.benchmark.draw.sourcelang]
                              .loc[data["targetlang"]==configuration.benchmark.draw.targetlang], 
                     x=configuration.benchmark.draw.x, 
                     y=configuration.benchmark.draw.y,
                     hue=configuration.benchmark.draw.hue,
                     log=configuration.benchmark.draw.log)
ax.set_ylabel("")
ax.set_xlabel(configuration.benchmark.draw.label)
ax.spines[['right', 'top']].set_visible(False)
ax.set_yticklabels([f"test {i:02d}" for i,_ in enumerate(ax.get_yticklabels())])

plt.rc('text', usetex=True )
plt.rc('font',family = 'sans-serif',  size=20)


fig.savefig(configuration.benchmark.draw.output_path,
            format=configuration.benchmark.draw.format,
            transparent=True)


