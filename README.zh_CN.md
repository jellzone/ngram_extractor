## 关键字分组工具
该程序是一个基于 Python 的 n-gram 提取器，用于处理 Excel 文件中的文本数据。 它分析输入文本，提取 n-gram（n 个单词的连续序列），并计算每个 n-gram 的频率。 然后将结果保存到一个输出 Excel 文件中，其中包含原始数据以及最常见的 n-gram 及其在每个文本条目中的频率。 此外，输出文件中的单独表格列出了所有唯一的 n-gram 及其频率。

## 特性
- 从 Excel 文件中读取输入数据
- 从文本中提取可变长度（2 到 5 个单词）的 n-gram
- 计算每个n-gram的频率
- 将结果保存到输出 Excel 文件
- 需要最少的用户输入并在未安装 Python 的 Windows 系统上运行
## 用法
- 确保输入文件 (输入数据.xlsx) 与可执行文件位于同一目录中。
- 通过双击或从命令行运行可执行文件 (ngram_extractor.exe) 来运行它。
- 该程序将处理输入数据并将结果保存到同一目录中的新 Excel 文件 (输出结果.xlsx)。
- 请保持输入数据里面表头是 “Title”，每一行都是不同的文本，程序会提取所有文本
## 要求
- Python 3.6 或更新版本
- pandas
- openpyxl安装要直接运行脚本，使用pip安装所需的包：
``pip instrall pandas openpyxl``

要将脚本打包为适用于 Windows 的独立可执行文件，请使用
``pyinstaller：pip install pyinstaller pyinstaller --onefile ngram_extractor.py``

打包的可执行文件将位于 dist 文件夹中。

[下载包windows版本](https://github.com/jellzone/ngram_extractor/releases/tag/windows)
