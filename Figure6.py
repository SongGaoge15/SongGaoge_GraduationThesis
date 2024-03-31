import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取文件
file_path = 'your_path_to_results.csv'  # 在此输入数据文件的路径
df = pd.read_csv(file_path)

# 进行图片布局
# sns.set_theme(style="ticks")  # 设置seaborn的绘图主题（可选）
plt.figure(figsize=(20/2.54, 10/2.54), dpi=600)  # 设置20×10cm、分辨率600dpi的画布

class_labels = ['Lac', 'Aeo', 'Coll', 'Fp', 'Flv']  # 设置沉积环境的类别标签

columns_to_plot = ['Phi', 'sigma', 'Skewness', 'Kurtosis']  # 在列表中输入需要可视化的数据列标题
title_labels = {'Phi': '(a)', 'sigma': '(b)', 'Skewness': '(c)', 'Kurtosis': '(d)'}  # 构建一个字典，用于设定子图的标题

y_axis_limits = [(-1, 7), (0, 5), (0, 7), (0, 70)]  # 确定各个子图的y轴范围

# 构建一个字典，用于标记不同沉积环境的颜色
color_mapping = {1: '#ACC97D',
                 2: '#CC8B3E',
                 3: '#FFC8DB',
                 4: '#5B5BC0',
                 5: '#54AFC3'}

# 绘图代码，使用for循环逐一绘制子图
for i, (column, limits) in enumerate(zip(columns_to_plot, y_axis_limits), 1):
    plt.subplot(1, 4, i)
    
    # 使用sns.boxplot函数绘制箱型图
    ax = sns.boxplot(x='class', y=column, data=df,
                     palette=color_mapping,
                     width=0.6,
                     fliersize=2.5,
                     linewidth=0.8)
    
    # 根据title_labels列表中的元素设置相应的子图标题，字体样式为11磅加粗Times New Roman
    plt.title(title_labels[column], fontsize=11, fontname='Times New Roman', fontweight='bold', loc='left')
    
    # 删去坐标轴标题
    plt.xlabel('')
    plt.ylabel('')
    
    # 设置x轴的刻度标签以及y轴的范围
    ax.set_xticklabels(class_labels, fontdict={'fontsize': 10, 'fontname': 'Times New Roman'})
    plt.ylim(limits)
    
    # 逐一更改y轴刻度标签的字体
    for label in ax.get_yticklabels():
        label.set_fontname('Times New Roman')
        label.set_fontsize(10)

# 图片导出
plt.tight_layout()
plt.savefig('Fig 6.png')
plt.show()