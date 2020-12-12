# xigua
解析西瓜视频地址并下载(可选择清晰度/预先设定标题)

## Requirements

- python >= 3.6

```bash
python -m pip -r requirements.txt
```

## Usage

```bash
python xigua.py
# 直接回车测试 https://www.ixigua.com/i6704446868685849092
输入西瓜链接：https://www.ixigua.com/6903456861337584142
# 开始解析
# Auto（输入 0 ）
# 360p （输入 1 ） :  640 x 360
# 480p （输入 2 ） :  854 x 480
# 720p （输入 3 ） :  1280 x 720
选择清晰度：0
# http://v3-default.ixigua.com/c561bad6191712f71aebe719d65d7ace/5fd51b1f/video/tos/cn/tos-cn-ve-4/ee826b26c74f45c399a3e170f0778083/?a=2012&br=3636&bt=1212&cd=0%7C0%7C0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=202012130221380102040550150E3E8569&lr=&mime_type=video_mp4&qs=0&rc=M3R2NHhuPDd5eTMzaTczM0ApZ2Y0NWg6PGVnNzk5ODQzOWcvZ2toZzY2bjNfLS1fLTBzc2AyYi02Y180LWItNmJiYjI6Yw%3D%3D&vl=&vr=
# 开始下载
# 【反击篇】1400亿，8次反转的中国6方财阀内斗：万科争夺战三部曲 - 西瓜视频.mp4下载33.56%---18.21M/s
# 【反击篇】1400亿，8次反转的中国6方财阀内斗：万科争夺战三部曲 - 西瓜视频.mp4下载58.30%---13.42M/s
# 【反击篇】1400亿，8次反转的中国6方财阀内斗：万科争夺战三部曲 - 西瓜视频.mp4下载81.73%---12.71M/s
# 下载完成
```

默认下载在当前目录。

基于 [xigua](https://github.com/py-wuhao/xigua)

