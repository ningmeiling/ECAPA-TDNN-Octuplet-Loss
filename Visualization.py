#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 20:45:39 2023
@author: ningmeiling
"""
import os
import matplotlib.pyplot as plt

# 数据
loss_functions = ['Triplet Loss', 'Octuplet Loss + AAM-softmax', 'Octuplet Loss']
eer = [41.59, 8.75, 1.62]
min_dcf = [0.9989, 0.5036, 0.1098]

# 创建第一个子图
plt.subplot(2, 1, 1)
plt.bar(loss_functions, eer, color=['#FFFACD', '#B0E0E6', '#FFB6C1'])  # 自定义颜色
plt.title('EER', fontsize=14, fontweight='bold')
plt.xlabel('Loss Function', fontsize=12)
plt.ylabel('Percentage', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--')

# 在图上标注数值（加上百分号符号）
for i in range(len(loss_functions)):
    plt.text(loss_functions[i], eer[i], f"{eer[i]}%", ha='center', va='bottom', fontsize=10)

# 创建第二个子图
plt.subplot(2, 1, 2)
plt.bar(loss_functions, min_dcf, color=['#FFFACD', '#B0E0E6', '#FFB6C1'])  # 自定义颜色
plt.title('minDCF', fontsize=14, fontweight='bold')
plt.xlabel('Loss Function', fontsize=12)
plt.ylabel('Percentage', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--')

# 在图上标注数值（加上百分号符号）
for i in range(len(loss_functions)):
    plt.text(loss_functions[i], min_dcf[i], f"{min_dcf[i]}%", ha='center', va='bottom', fontsize=10)

# 调整子图之间的间距
plt.tight_layout()

# 保存图像到桌面（dpi参数用于设置图像分辨率）
desktop_path = os.path.expanduser("~/Desktop")
save_path = os.path.join(desktop_path, "bar_plot.png")
plt.savefig(save_path, dpi=300)

# 显示图形
plt.show()
