# Welcome to [SongGaoge_GraduationThesis](https://github.com/SongGaoge15/SongGaoge_GraduationThesis/tree/main)!

该github仓库存储了毕业论文写作过程中所需的模型训练与制图代码，便于有需要的老师、同学开源获取。本论文在代码撰写的部分采用了**ChatGPT 4**辅助开发。

## 绘图代码
论文中的多数插图是基于**Python 3.12**绘制的，作者在撰写代码的过程中采用的IDE是**Spyder**，其它值得推荐的IDE也包括**PyCharm**、**Jupyter Notebook**等。

如果要配置Python环境用于绘制论文插图或其它数据分析工作，比较推荐的方式是使用[Anaconda](https://www.anaconda.com/)并配置虚拟环境，这是由于Anaconda在建立虚拟环境时，可以比较好地处理各个包之间的依赖关系，从而使得代码及环境更易于管理，同时也能较好地照顾到兼容性。

### Fig. 3 典型样本的粒度分布与粒度参数

图3 (a)至图3 (e)展示了训练集中分属不同沉积环境的**训练样本的粒度曲线**，并基于这些粒度曲线计算了各个沉积环境的**平均曲线**。此外，图3 (f)分沉积环境显示了不同粒度参数的**带有误差棒的条形图**，以便对各类训练样本的粒度参数进行直观的理解。

需要注意的是，这段代码中，我们假设所需的数据存储在了同一个Excel表格的不同Sheet中。如果你的数据是以`.csv`格式存储的，则需要在代码读取数据的部分进行如下修改（但仍然可以通过导入的`pandas`包实现）：
``` Python
# 导入的包不变
# 假设原代码中的3个Sheet现在分别存储在training_data.csv、original_data.csv、grain_size_analysis.csv中

training_data_path = 'your_path_to/training_data.csv'
original_data_path = 'your_path_to/original_data.csv'
grain_size_analysis_path = 'your_path_to/grain_size_analysis.csv'

training_data = pd.read_csv(training_data_path)
original_data = pd.read_csv(original_data_path)
grain_size_analysis = pd.read_csv(grain_size_analysis_path)

# 后续的代码不变
```

### Fig. 6 不同沉积环境的粒度参数箱型图
图6展示了不同沉积环境的粒度参数，并采用**箱型图**来体现各个粒度参数在不同沉积环境中所表现的分散特征。

进行图形绘制前，请按下述结构组织数据：
| Specimen | Phi | sigma | Skewness | Kurtosis | Class |
|--|--|--|--|--|--|
| Spec 1 | 3.2127 | 2.2156 | 2.3145 | 7.1175 | 5 |
| Spec 2 | 2.4790 | 1.9923 | 2.6787 | 9.7047 | 5 |
| …… | …… | …… | …… | …… | …… |

代码运行时，将按照沉积环境分类变量`Class`的取值，分别绘制不同沉积环境的粒度参数（示例中，这些参数包括`Phi`、`sigma`、`Skewness`、`Kurtosis`）。

要运行此代码，需要安装的包包括`matplotlib`、`seaborn`、`pandas`，你可以在Anaconda Prompt中运行以下命令：
 - 激活相应的环境：`conda activate your_env_name`
 - 安装相应的包：`conda install matplotlib seaborn pandas`

需要注意，如果你的虚拟环境中没有配置所需的包，代码运行时将报错。
