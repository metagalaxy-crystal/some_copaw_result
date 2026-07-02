# 🎬 小说动画生成器 - 快速使用指南

## 📍 文件位置

```
~/Desktop/skills/novel-animation/
├── SKILL.md          # 完整技能文档
├── generate.sh       # 主启动脚本
├── generator.py      # Python 生成器
└── README.md         # 本文件
```

---

## 🚀 快速开始

### 方法 1：一键生成（推荐）

```bash
cd ~/Desktop/skills/novel-animation
./generate.sh
```

这将生成：
- ✅ 赛博朋克短篇小说（约 1000 字）
- ✅ 配套动画（GIF + MP4）
- ✅ 封面图片

### 方法 2：自定义参数

```bash
./generate.sh --genre cyberpunk --length short --output both
```

**参数说明：**

| 参数 | 选项 | 默认值 |
|------|------|--------|
| `--genre` | cyberpunk / fantasy / thriller | cyberpunk |
| `--length` | short / medium / long | short |
| `--output` | mp4 / gif / both | both |

### 方法 3：直接运行 Python

```bash
python3 generator.py --genre cyberpunk --output mp4
```

---

## 📁 输出文件

生成完成后，桌面会出现以下文件：

```
~/Desktop/
├── 霓虹深渊_赛博朋克小说.md    ← 小说文本
├── 霓虹深渊_赛博朋克动画.mp4   ← 动画视频
├── 霓虹深渊_赛博朋克动画.gif   ← 动画 GIF
└── 霓虹深渊_赛博朋克动画_封面.png ← 封面图
```

---

## ⚙️ 依赖安装

首次运行前，确保已安装依赖：

```bash
# 基础依赖
pip3 install matplotlib numpy pillow

# 可选：MP4 输出支持
sudo apt-get install ffmpeg
```

---

## 🎨 动画风格预览

### 赛博朋克 (Cyberpunk)
- 🌃 未来都市天际线
- 🌧️ 动态雨滴效果
- 🚁 飞行汽车穿梭
- 💾 数据流可视化
- ✨ 霓虹灯闪烁

### 奇幻 (Fantasy) - 即将支持
- 🏰 城堡剪影
- ⭐ 魔法粒子
- 🌙 星空背景

### 悬疑 (Thriller) - 即将支持
- 🌫️ 迷雾效果
- 💡 闪烁灯光
- 🖤 暗色调

---

## 💡 使用场景

1. **内容创作** - 快速生成短视频素材
2. **写作辅助** - 可视化故事场景
3. **教学演示** - 生动的课堂材料
4. **创意实验** - 探索 AI 创作边界

---

## 🔧 故障排除

### 问题：中文字体显示异常
```bash
# 安装中文字体
sudo apt-get install fonts-wqy-microhei
```

### 问题：MP4 无法保存
```bash
# 安装 ffmpeg
sudo apt-get install ffmpeg

# 或改用 GIF 输出
./generate.sh --output gif
```

### 问题：动画太卡
```python
# 编辑 generator.py，降低帧数
frames=100  # 原为 200
dpi=80      # 原为 100
```

---

## 📖 完整文档

详细技术文档请参阅 `SKILL.md`

---

## 🎉 开始创作吧！

```bash
./generate.sh --help  # 查看所有选项
./generate.sh         # 一键生成
```

祝你创作愉快！✨