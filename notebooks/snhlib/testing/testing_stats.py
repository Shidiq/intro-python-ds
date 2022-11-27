from snhlib.stats import Bootstrap
import numpy as np

arr = [8, 5, 4, 6, 2]
boot = Bootstrap(estimator=np.mean, random_state=3, bootsample=1000)

boot_sample = boot.generate_bootstrap(arr)

fig = boot.plot_bootstrap(arr)
fig.show()

plt = boot.plot_hist(arr)
plt.show()