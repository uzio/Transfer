## [*] 本文件集合是angr多进程并行路径探索实现项目的虚拟环境的依赖包和测试用例

### 多进程改动后的程序文件及环境配置：

通过virtualenv + virtualenvwrapper(windows环境下为virtualenvarapper-win)模块，创建新的python虚拟环境，打开虚拟环境的安装路径，将Lib目录用该压缩包解压后替换

### 测试用例运行：

进入测试用例目录，通过切换原始的angr环境和多进程改动后的angr环境，分别运行find2.py

正常运行结束后，程序会返回求解结果和合计运行用时