import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

# 读取数据
# 需要注意的是，这里假设数据存储在xlsx格式的Excel表格中；如果你的数据以csv格式存储，请参阅README.md中的相应部分修改
file_path = 'your_path_to_excel_file.xlsx'
training_data = pd.read_excel(file_path, sheet_name='training_set_sheet')  # 训练集中包含训练样本的经标准化的粒度参数与沉积环境
original_data = pd.read_excel(file_path, sheet_name='original_data_sheet')  # 原始数据集中包含样本未经标准化的粒度参数
grain_size_analysis = pd.read_excel(file_path, sheet_name='grain_size_data_sheet')  # 粒度数据集中包含样本的粒度原始测量数据

dataframes_by_class = {i: pd.DataFrame() for i in range(1, 6)}

for index, row in training_data.iterrows():
    specimen = row['Specimen']
    class_label = row['Class']
    
    specimen_data = original_data[original_data['Specimen'] == specimen]
    if not specimen_data.empty:
        if dataframes_by_class[class_label].empty:
            dataframes_by_class[class_label] = specimen_data
        else:
            dataframes_by_class[class_label] = pd.concat([dataframes_by_class[class_label], specimen_data], ignore_index=True)

# 初始化一个用于存储统计结果的字典
statistics_by_class = {}

# 指定需要计算统计特征的参数
parameters = ['Phi', 'sigma', 'Skewness', 'Kurtosis']

# 遍历每个类别
for class_label, df in dataframes_by_class.items():
    class_specimens = df['Specimen']  # 获取当前类别对应的样本编号
    class_data = grain_size_analysis[grain_size_analysis['Specimen'].isin(class_specimens)]  # 从grain_size_analysis中选取当前沉积环境的样本数据
    stats = {param: {} for param in parameters}  # 初始化存储当前类别统计数据的字典
    
    # 对于每个参数，计算统计特征
    for param in parameters:
        stats[param]['mean'] = class_data[param].mean()
        stats[param]['std'] = class_data[param].std()
        stats[param]['min'] = class_data[param].min()
        stats[param]['max'] = class_data[param].max()
        stats[param]['median'] = class_data[param].median()
    
    # 将当前类别的统计数据存储到结果字典中
    statistics_by_class[class_label] = stats

# 将不同沉积环境的各个粒度参数统计指标输出到控制台
for class_label, stats in statistics_by_class.items():
    print(f"Class {class_label}:")
    for param, values in stats.items():
        print(f"  {param}:")
        for stat, value in values.items():
            rounded_value = round(value, 2)
            print(f"    {stat}: {rounded_value}")
    print("\n")

# 创建18×26cm、分辨率600dpi的画布
fig = plt.figure(figsize=(18/2.54, 26/2.54), dpi=600)

# 对前5个绘制不同沉积环境粒度参数的子图，设置其坐标轴标题与图题
x_labels = 'Φ'  # x轴标题为“Φ”
y_labels = '体积分数（%）'  # y轴标题为“体积分数（%）”
class_labels = ['(a)', '(b)', '(c)', '(d)', '(e)']  # 子图标题从(a)到(e)

# matplotlib中的gridspec方法提供了分割子图的功能，在这里建立一个3行2列的子图布局
gs = gridspec.GridSpec(3, 2)

phi_values = -np.log2(original_data.columns[1:-2].astype(float) / 1000)  # 将μm尺度的粒径转换为Φ尺度
sample_counts = {class_label: df.shape[0] for class_label, df in dataframes_by_class.items()}  # 分别统计一下各个沉积环境的样本数

# 循环绘制第1-5个子图
for class_idx, (class_label, df) in enumerate(dataframes_by_class.items(), start=1):
    if class_idx <= 5:  # 这一判断条件可以确保绘制时跳过第6个子图
        ax = fig.add_subplot(gs[(class_idx-1) // 2, (class_idx-1) % 2])  # 为每个子图创建一个坐标轴实例
        class_specimens = df['Specimen']  # 抽取出当前沉积环境数据帧中的样本编号
        class_data = original_data[original_data['Specimen'].isin(class_specimens)]  # 根据样本编号，获取每一个粒级测量点上的数据
        
        mean_volume_fractions = class_data.iloc[:, 1:-2].mean(axis=0)  # 计算均值
        
        # 逐一绘制同一沉积环境中，每个训练样本的粒度曲线
        for index, row in df.iterrows():
            volume_fractions = row[1:-2].values
            ax.plot(phi_values, volume_fractions,  # 曲线上点的横纵坐标分别为各测量点的Φ值与对应的体积分数
                    color='black',  # 曲线颜色设为黑色
                    alpha=0.5,  # 曲线透明度设为50%
                    linewidth=0.5,  # 曲线宽度设为0.5
                    linestyle='-',  # 曲线样式设为单一实线
                    marker='', markersize=0)  # 不显示曲线上的数据点
        
        # 单独绘制平均粒度曲线
        ax.plot(phi_values, mean_volume_fractions,  # 曲线上点的横纵坐标分别为各测量点的Φ值与对应的平均体积分数
                color='magenta',  # 曲线颜色设为品红色
                linewidth=2,  # 曲线宽度设为2
                linestyle='--',  # 曲线样式设为虚线
                marker='', markersize=0)  # 不显示曲线上的数据点
        
        ax.set_xlim(-2, 14)  # 横轴范围限定在-2~14
        ax.set_ylim(0, 15)  # 纵轴范围限定在0~15
        
        # 设置x轴和y轴的刻度，并将字体设为10磅Times New Roman
        plt.xticks(range(-2,16,2), fontname='Times New Roman', fontsize=10)
        plt.yticks(range(0,20,5), fontname='Times New Roman', fontsize=10)
        
        # 显示y轴上的刻度线，样式为宽度0.25的灰色虚线
        ax.grid(axis='y', color='gray', linestyle='--', linewidth=0.25)
        
        # 设置坐标轴的标题样式
        ax.set_xlabel(x_labels, fontname='Times New Roman', fontsize=10)  # x轴标题为10磅Times New Roman
        ax.set_ylabel(y_labels, fontname='SimSun', fontsize=10)  # y轴标题为10磅宋体（SimSun）
        
        # 标注当前沉积环境的样本数，以“N = sample_count”形式标注，字体为10磅Times New Roman
        sample_count = sample_counts[class_label]
        ax.text(0.95, 0.95, f'N = {sample_count}', transform=ax.transAxes, 
                horizontalalignment='right', verticalalignment='top',
                fontdict={'fontsize': 10, 'fontname': 'Times New Roman'})
        
        # 标注子图标题
        ax.set_title(class_labels[class_idx - 1], 
                     loc='left',  # 设置左侧放置
                     fontdict={'family':'Times New Roman', 'weight':'bold', 'size':11})  # 字体为11磅加粗Times New Roman

# 初始化一个用于存储不同沉积环境的粒度参数平均值（mean）和标准误（sem）的字典
class_stats = {class_label: {'mean': [], 'sem': []} for class_label in range(1, 6)}

# 使用for循环遍历沉积环境，并计算相关统计指标
for class_label, df in dataframes_by_class.items():
    class_specimens = df['Specimen']
    class_data = grain_size_analysis[grain_size_analysis['Specimen'].isin(class_specimens)]
    
    for parameter in ['Phi', 'sigma', 'Skewness', 'Kurtosis']:
        class_stats[class_label]['mean'].append(class_data[parameter].mean())
        class_stats[class_label]['sem'].append(class_data[parameter].sem())

ax = fig.add_subplot(gs[2, 1])  # 创建条形图子图

parameters = ['平均粒径', '分选系数', '偏度', '峰度']  # 列表parameters中的元素将作为x轴的4组标签

x = np.arange(len(parameters))  # x轴的位置
width = 0.15  # 设置条形图的条宽度
class_name = ['湖沼相', '风沙相', '残坡积相', '洪流相', '河床相']  # 使用class_name列表存储不同图例的标注
ax.grid(axis='y', color='gray', linestyle='--', linewidth=0.25)  # 设置条形图的背景网格，样式为宽度0.25的灰色虚线

# 使用for循环为每个沉积环境绘制柱状图
for class_label, stats in class_stats.items():
    ax.bar(x + width * (class_label - 3), stats['mean'], width, alpha=0.8, label=class_name[class_label-1], yerr=stats['sem'], capsize=2, error_kw={'linewidth': 0.5})

# 设置坐标轴的标题（可选）
# ax.set_xlabel('粒度参数', fontname='SimSun', fontsize=10)
# ax.set_ylabel('值', fontname='SimSun', fontsize=10)

# 子图标题为“(f)”，样式为11磅加粗Times New Roman，在左侧放置
ax.set_title('(f)', loc='left', fontdict={'family':'Times New Roman', 'weight':'bold', 'size':11})

ax.set_xticks(x)  # 根据第140行的x轴位置加注x轴刻度标签
ax.set_ylim(0, 22)  # 纵轴范围限定在0~22
plt.yticks(range(0,23,2), fontname='Times New Roman', fontsize=10)  # y轴刻度为10磅Times New Roman
ax.set_xticklabels(parameters, fontname='SimSun', fontsize=10, rotation=45)  # x轴刻度为10磅宋体（SimSun），并旋转45°

# 加注图例，透明度为100%，边框颜色为灰色，字体为10磅宋体（SimSun）
ax.legend(framealpha=1, edgecolor='gray', prop={'family':'SimSun', 'size':10})

# 导出图片
plt.tight_layout()
plt.savefig('Fig 3.png')
plt.show()