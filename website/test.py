import re

jingsi_dict = {}

with open('./website/t1.txt', encoding='utf-8') as f:
    for line in f:
        g = re.split('、', line)
        jingsi_dict[int(g[0])] = g[1]