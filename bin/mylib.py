class Style:
    @staticmethod
    def update():
        plt.style.use("classic")
        params = {
            "axes.formatter.useoffset": False,
            "font.family": "sans-serif",
            "font.sans-serif": "Arial",
            "xtick.labelsize": 28,
            "ytick.labelsize": 28,
            "axes.labelsize": 28,
            "axes.labelweight": "bold",
            "axes.titlesize": 28,
            "axes.titleweight": "bold",
            "figure.dpi": 300,
            # "figure.figsize": figsize,
            # "legend.loc": loc,
            "legend.fontsize": 24,
            "legend.fancybox": True,
            "mathtext.fontset": "custom",
            "mathtext.default": "regular",
            "figure.autolayout": False,
            "patch.edgecolor": "#000000",
            "text.color": "#000000",
            "axes.edgecolor": "#000000",
            "axes.labelcolor": "#000000",
            "xtick.color": "#000000",
            "ytick.color": "#000000",
        }
        matplotlib.rcParams.update(params)
        
    @staticmethod
    def reset():
        matplotlib.rcParams.update(matplotlib.rcParamsDefault)