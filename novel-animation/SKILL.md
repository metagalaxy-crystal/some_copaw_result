# Novel Animation Generator / 小说动画生成器

## 技能描述

**自动生成小说并制作配套动画**

本技能帮助用户：
1. 创作短篇科幻小说（赛博朋克/奇幻/悬疑等类型）
2. 根据小说主题生成匹配风格的动画
3. 输出完整的故事文件 + 动画视频/GIF

**适用场景：**
- 快速创作故事并可视化
- 制作短视频内容
- 创意写作辅助
- 教学演示材料

---

## 触发词

| 触发词/场景 | 说明 |
|------------|------|
| 写小说 + 动画 | 核心触发 |
| 生成故事动画 | 故事可视化 |
| 创作短视频 | 内容创作 |
| 小说场景动画化 | 场景可视化 |
| cyberpunk story | 赛博朋克故事 |
| 科幻动画 | 科幻类型 |

---

## 使用方法

### 基础调用

```bash
# 进入技能目录
cd /home/junsheng/Desktop/skills/novel-animation

# 运行生成器
bash generate.sh
```

### 带参数调用

```bash
# 指定类型和长度
bash generate.sh --genre cyberpunk --length short --output mp4

# 参数说明
# --genre: cyberpunk | fantasy | romance | thriller | fairy
# --length: short (1000 字) | medium (3000 字) | long (5000 字)
# --output: mp4 | gif | both
```

### 自定义小说内容

```bash
# 提供你的故事大纲
bash generate.sh --prompt "一个关于时间旅行的故事，主角是..."

# 或直接替换 story_template.md 后运行
```

---

## 输出文件

| 文件 | 说明 | 默认位置 |
|------|------|----------|
| `{小说标题}_小说.md` | 完整小说文本 | ~/Desktop/ |
| `{小说标题}_动画.mp4` | 赛博朋克风格动画 | ~/Desktop/ |
| `{小说标题}_动画.gif` | GIF 格式备选 | ~/Desktop/ |
| `{小说标题}_封面.png` | 静态封面图 | ~/Desktop/ |

---

## 动画风格配置

### 赛博朋克 (Cyberpunk)
- **配色**: 霓虹青 (#00ffff)、霓虹粉 (#ff00ff)、深紫 (#9d00ff)
- **元素**: 未来城市、飞行汽车、数据流、雨滴、霓虹灯
- **适用**: 科幻、高科技低生活、AI 主题

### 奇幻 (Fantasy)
- **配色**: 金色、翠绿、深红
- **元素**: 魔法粒子、星空、城堡剪影
- **适用**: 魔法、冒险、中世纪主题

### 悬疑 (Thriller)
- **配色**: 深灰、暗红、冷蓝
- **元素**: 阴影、迷雾、闪烁灯光
- **适用**: 侦探、恐怖、心理主题

---

## 依赖项

### Python 库
```bash
pip3 install matplotlib numpy pillow
# 可选：用于 MP4 输出
sudo apt-get install ffmpeg
```

### 系统要求
- Python 3.7+
- Matplotlib 3.5+
- Pillow 9.0+

---

## 技术架构

```
novel-animation/
├── SKILL.md              # 技能说明（本文件）
├── generate.sh           # 主执行脚本
├── novel_generator.py    # 小说生成模块
├── animation_generator.py # 动画生成模块
├── templates/            # 故事模板
│   ├── cyberpunk.md
│   ├── fantasy.md
│   └── thriller.md
└── assets/               # 资源文件
    └── fonts/
```

---

## 示例输出

### 小说片段
```
《霓虹深渊》

公元 2147 年，新上海。

林夜站在「天穹塔」第 308 层的边缘，俯瞰着脚下
这片永不沉睡的钢铁丛林。霓虹灯海在酸雨雾霭中
漾开，青色、洋红、电紫的光晕交织成一张巨大的网...
```

### 动画效果
- 🌃 25 座未来建筑构成的天际线
- 🌧️ 200+ 动态雨滴
- 🚁 5 辆飞行汽车穿梭
- 💾 15 条数据流（代表意识上传）
- ✨ 霓虹灯闪烁效果
- 📝 动态标题展示

---

## 自定义扩展

### 添加新的动画风格

编辑 `animation_generator.py`：

```python
STYLE_CONFIGS = {
    'cyberpunk': {
        'colors': {...},
        'elements': ['buildings', 'cars', 'rain']
    },
    'fantasy': {
        'colors': {...},
        'elements': ['castle', 'stars', 'magic']
    },
    # 添加新风格
}
```

### 添加新的小说类型

在 `templates/` 下创建新的模板文件，定义：
- 故事结构
- 典型情节
- 角色原型
- 常用设定

---

## 常见问题

### Q: MP4 输出失败怎么办？
A: 安装 ffmpeg：`sudo apt-get install ffmpeg`
   或改用 GIF 输出：`--output gif`

### Q: 中文字体显示异常？
A: 确保系统已安装中文字体，或修改 matplotlib 字体配置

### Q: 动画渲染太慢？
A: 降低帧数或分辨率：
   ```python
   frames=100  # 减少帧数
   dpi=80      # 降低分辨率
   ```

### Q: 如何让小说更长？
A: 修改 `--length` 参数，或提供详细故事大纲

---

## 版本历史

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| 1.0 | 2026-05-03 | 初始版本，支持赛博朋克风格 |
| 1.1 | TBD | 添加奇幻/悬疑风格 |
| 1.2 | TBD | 支持自定义故事大纲 |

---

## 许可证

MIT License - 可自由使用和修改

---

## 作者笔记

这个技能的核心是将创意写作与视觉化结合。每次生成都是独特的，因为：
- 小说情节随机生成（可定制）
- 动画元素位置随机
- 颜色搭配有变化

享受创作的乐趣！🎬📝