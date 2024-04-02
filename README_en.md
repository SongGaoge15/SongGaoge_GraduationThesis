# Welcome to [SongGaoge_GraduationThesis](https://github.com/SongGaoge15/SongGaoge_GraduationThesis/tree/main)!

This GitHub repository stores the model training and diagram generation code required during the thesis writing process, making it openly accessible to interested teachers and students. The coding portion of this thesis utilized **ChatGPT 4** to assist in development.

## Drawing Codes
The majority of the illustrations in the paper were created using **Python 3.12**. The Integrated Development Environment (IDE) employed by the authors during the coding process was **Spyder**, with other recommendable IDEs including **PyCharm** and **Jupyter Notebook**.

For configuring a Python environment for creating paper illustrations or other data analysis tasks, the recommended approach is to use [Anaconda](https://www.anaconda.com/) and set up a virtual environment. This recommendation stems from Anaconda's adept handling of dependencies among packages when establishing virtual environments, thereby facilitating more manageable code and environment maintenance, as well as better compatibility.

### Fig. 3
Figures 3 (a) to 3 (e) showcase **the grain size curves** of training samples from different sedimentary environments contained within the training set, and based on these curves, **the average curve** for each sedimentary environment has been calculated. Additionally, Figure 3 (f) displays **bar charts with error bars** for different grain size parameters by sedimentary environment, facilitating an intuitive understanding of the granularity parameters of various classes of training samples.

It is important to note that in this code segment, it is assumed that the required data is stored in different sheets of the same Excel workbook. If your data is stored in `.csv` format, modifications will be needed in the part of the code that reads the data. However, this can still be accomplished by importing the `pandas` package, as demonstrated below:

```Python
# The imported packages remain unchanged
# Assuming the 3 Sheets from the original code are now stored in training_data.csv, original_data.csv, grain_size_analysis.csv respectively

training_data_path = 'your_path_to/training_data.csv'
original_data_path = 'your_path_to/original_data.csv'
grain_size_analysis_path = 'your_path_to/grain_size_analysis.csv'

training_data = pd.read_csv(training_data_path)
original_data = pd.read_csv(original_data_path)
grain_size_analysis = pd.read_csv(grain_size_analysis_path)

# The subsequent code remains unchanged
```

### Fig. 6 不同沉积环境的粒度参数箱型图
Figure 6 displays the granularity parameters of different depositional environments and employs **box plots** to illustrate the dispersion characteristics of each grain size parameter across various sedimentary environments.

Before proceeding with the graphical representation, please organize your data according to the following structure:
| Specimen | Phi | sigma | Skewness | Kurtosis | Class |
|--|--|--|--|--|--|
| Spec 1 | 3.2127 | 2.2156 | 2.3145 | 7.1175 | 5 |
| Spec 2 | 2.4790 | 1.9923 | 2.6787 | 9.7047 | 5 |
| …… | …… | …… | …… | …… | …… |

When running the code, grain size parameters (in this example, `Phi`, `sigma`, `Skewness`, `Kurtosis`) for different sedimentary environments will be drawn separately based on the values of the classification variable `Class` representing these environments.

To run this code, the packages `matplotlib`, `seaborn`, and `pandas` need to be installed. You can execute the following commands in Anaconda Prompt to set up your environment:

 - Activate the relevant environment: `conda activate your_env_name`
 - Install the necessary packages: `conda install matplotlib seaborn pandas`

Please be aware that if your virtual environment does not have the required packages configured, attempting to run the code will result in errors.
