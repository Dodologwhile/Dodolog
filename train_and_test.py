#!/usr/bin/env python
# coding: utf-8
# 检查数据集所在路径
get_ipython().system('tree -L 3 /home/aistudio/data ')

# ## 下载PaddleVideo代码

# 进入到gitclone 的PaddleVideo目录下
get_ipython().run_line_magic('cd', '~/work/')

# 从Github上下载PaddleVideo代码
#!git clone https://github.com/PaddlePaddle/PaddleVideo.git
# 若网速较慢，可使用如下方法下载
get_ipython().system('git clone https://hub.fastgit.org/PaddlePaddle/PaddleVideo.git')

# 进入到gitclone 的PaddleVideo目录下
get_ipython().run_line_magic('cd', '~/work/PaddleVideo/')

# 检查源代码文件结构
get_ipython().system('tree /home/aistudio/work/ -L 2')

# ## 配置代码环境，安装相应的依赖包

get_ipython().system('python3.7 -m pip install --upgrade pip')
get_ipython().system('python3.7 -m pip install --upgrade -r requirements.txt')


# ## 设置配置文件，完成行为识别算法训练
# 
# PaddleVideo 通过yaml配置文件的方式选择不同的算法和训练参数等，这里我们使用`configs/recognition/stgcn/stgcn_fsd.yaml`配置文件完成ST-GCN模型算法训练。从该配置文件中，我们可以得到如下信息：
#

get_ipython().system('python3.7 main.py -c configs/recognition/stgcn/stgcn_fsd.yaml')

# ## 测试脚本
# 模型训练完成后，可使用测试脚本进行评估，
get_ipython().system('python3.7 main.py --test -c configs/recognition/stgcn/stgcn_fsd.yaml -w output/STGCN/STGCN_epoch_00090.pdparams')

get_ipython().system('wget https://videotag.bj.bcebos.com/PaddleVideo-release2.2/STGCN_fsd.pdparams')

# 通过-w参数指定模型权重进行测试
get_ipython().system('python3.7 main.py --test -c configs/recognition/stgcn/stgcn_fsd.yaml -w STGCN_fsd.pdparams')

# 测试脚本运行完成后，可以在当前目录中得到`submission.csv`文件，将该文件提交至[评测官网](https://aistudio.baidu.com/aistudio/competition/detail/115)，即可以查看在A榜得分。示例给出的模型文件，在A榜的得分为59.07。


