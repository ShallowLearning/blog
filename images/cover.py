import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white", palette="muted")
with plt.xkcd():
    #f, axes = plt.subplots(2, 1, figsize=(2.5, 5))
    #f.set_facecolor('black')
    f = plt.figure()
    rs = np.random.RandomState(50)
    x, y = rs.randn(2, 50)

    #cmap = sns.cubehelix_palette(start=2, light=1, as_cmap=True)
    #sns.kdeplot(x, y, cmap=cmap, shade=True, ax=axes[1])
    
    b, g, r, p = sns.color_palette("muted", 4) 
    d = rs.normal(size=100)
    sns.distplot(d, color=b)#, ax=axes[0])

    #axes[1].axis('off')

    #for ax, s in zip(axes.flat, np.linspace(0, 3, 10)):
    #    x, y = rs.randn(2, 50)
    #    cmap = sns.cubehelix_palette(start=s, light=1, as_cmap=True)
    #    sns.kdeplot(x, y, cmap=cmap, shade=True, cut=5, ax=ax)

    f.tight_layout()
    f.savefig('cover_image_sns.svg')
