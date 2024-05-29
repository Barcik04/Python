Kernel Density Estimation plot (kde)
        import seaborn as sns
        import numpy as np
        import matplotlib.pyplot as plt
        data = np.random.randn(1000)
        sns.kdeplot(data, fill=True)
        plt.show()


Wykres pudełkowy (boxplot)
        import numpy as np
        import matplotlib.pyplot as plt
        data = [np.random.normal(0, std, 100) for std in range(1, 4)]
        plt.boxplot(data)
        plt.show()


Wykres obszarowy (area plot)
        import numpy as np
        import matplotlib.pyplot as plt
        import pandas as pd
        
        df = pd.DataFrame({
            'A': np.random.rand(10),
            'B': np.random.rand(10),
            'C': np.random.rand(10)
        })
        df.plot.area()
        plt.show()



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({
    'x': np.random.randn(1000),
    'y': np.random.randn(1000)
})
df.plot.hexbin(x='x', y='y', gridsize=25)
plt.show()
