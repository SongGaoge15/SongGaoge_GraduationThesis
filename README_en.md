# Welcome to [SongGaoge_GraduationThesis](https://github.com/SongGaoge15/SongGaoge_GraduationThesis/tree/main)!

This GitHub repository stores the model training and diagram generation code required during the thesis writing process, making it openly accessible to interested teachers and students. The coding portion of this thesis utilized **ChatGPT 4** to assist in development.

## Drawing Codes
The majority of the illustrations in the paper were created using **Python 3.12**. The Integrated Development Environment (IDE) employed by the authors during the coding process was **Spyder**, with other recommendable IDEs including **PyCharm** and **Jupyter Notebook**.

For configuring a Python environment for creating paper illustrations or other data analysis tasks, the recommended approach is to use [Anaconda](https://www.anaconda.com/) and set up a virtual environment. This recommendation stems from Anaconda's adept handling of dependencies among packages when establishing virtual environments, thereby facilitating more manageable code and environment maintenance, as well as better compatibility.

### Fig. 6 不同沉积环境的粒度参数箱型图
Figure 6 displays the granularity parameters of different depositional environments and employs **box plots** to illustrate the dispersion characteristics of each grain size parameter across various sedimentary environments.

Before proceeding with the graphical representation, please organize your data according to the following structure:
| Specimen | Phi | sigma | Skewness | Kurtosis | Class |
|--|--|--|--|--|--|
| Spec 1 | 3.2127 | 2.2156 | 2.3145 | 7.1175 | 5 |
| Spec 2 | 2.4790 | 1.9923 | 2.6787 | 9.7047 | 5 |
| …… | …… | …… | …… | …… | …… |

When running the code, granularity parameters (in this example, Phi, sigma, Skewness, Kurtosis) for different depositional environments will be drawn separately based on the values of the classification variable Class representing these environments.

To run this code, the packages matplotlib, seaborn, and pandas need to be installed. You can execute the following commands in Anaconda Prompt to set up your environment:

 - Activate the relevant environment: `conda activate your_env_name`
 - Install the necessary packages: `conda install matplotlib seaborn pandas`

Please be aware that if your virtual environment does not have the required packages configured, attempting to run the code will result in errors.
