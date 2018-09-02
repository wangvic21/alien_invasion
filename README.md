# Alien_Invasion
---
### Table of Contents
* [简介](#简介)
* [文件目录](#文件目录)
* [运行环境](#运行环境)
	* [运行说明](#运行说明)
	* [Pygame安装说明](#Pygame安装说明)


## 简介
这是一个利用Python3编写的飞船设计外星人的游戏。主要利用的是Python的Pygame模块。

## 文件目录
```
.
├── README.md
├── alien.py
├── alien_invasion.py
├── bullet.py
├── button.py
├── game_functions.py
├── game_stats.py
├── high_score.json
├── images
│   ├── alien.bmp
│   └── ship.bmp
├── scoreboard.py
├── settings.py
└── ship.py
1 directory, 13 files
```
* alien_invasion.py是主程序模块，调用了Alien、Bullet、Ship等类。
* game_functions.py是游戏功能实现模块，包含了检测按键、更新界面、存储数据等功能。
* settings存储了游戏的相关设置，包括界面大小，飞船、子弹、外星人的速度等参数。
* high_score.json存储了游戏的最高分，在不存在的情况下可以自动生成。

## 运行环境
* Python3
* Pygame模块

### 运行说明
* P或者点击Play开始游戏
* Q或者点击窗口“X”关闭游戏

### Pygame安装说明
#### 安装pip
1. Linux & OS X
	* 检测pip是否安装

		```
		$ pip3 --version
		
		pip 10.0.1 from /Library/.../site-packages/pip (python 3.7)
		```
	* 安装pip
	
	 下载[get-pip.py](https://bootstrap.pypa.io/get-pip.py)。
	 在终端运行
	 
	 ```
	 sudo python3 get-pip.py
	 ```
2. Windows
	* 检测pip是否安装

		```
		$ python -m pip --version

		```
	* 安装pip
	
	 下载[get-pip.py](https://bootstrap.pypa.io/get-pip.py)。
	 在终端运行
	 
	 ```
	 python get-pip.py
	 ```

#### 安装pygame
1. OS X & Linux
	
	```
	pip3 install pygame
	```
2. Windows

	访问[Python Extension Packages for Windows](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame.)下载pygame，注意版本。

	
