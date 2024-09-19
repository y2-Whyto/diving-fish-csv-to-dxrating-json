# diving-fish.com CSV \(maimai DX\) → dxrating.net JSON

[在水鱼查分器中导出.csv舞萌成绩](https://www.diving-fish.com/maimaidx/prober/#Export)后，使用本脚本可以转换为dxrating.net格式的.json成绩，用于[在dxrating.net上传](https://dxrating.net/rating)。

> （虽然感觉好像传了也没什么luan用）

## 用法

```shell
git clone https://github.com/y2-Whyto/diving-fish-maimai-csv-to-dxrating-json.git
cd diving-fish-maimai-csv-to-dxrating-json
python score_convert.py -i input.csv -o output.json
```

`input.csv`是输入的csv文件名，`output.json`是输出的json文件名。请根据实际情况替换。

可以使用`-h`或`--help`开关查看帮助说明。

## 注意

使用时如果`output.json`文件已存在，则会**无提示直接覆盖**。如需保留原文件，请提前自行备份。

## 鸣谢

**TEfish**——测试工作
