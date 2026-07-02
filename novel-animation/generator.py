#!/usr/bin/env python3
"""
Novel & Animation Generator
小说与动画生成器 - 核心模块
"""

import argparse
import random
import os
from datetime import datetime

# ============== 小说生成模块 ==============

NOVEL_TEMPLATES = {
    'cyberpunk': {
        'title': '霓虹深渊',
        'setting': '2147 年新上海',
        'protagonist': '林夜',
        'conflict': '意识上传与数字自由',
        'themes': ['科技与人性的边界', '记忆与身份', '企业控制 vs 个人自由']
    },
    'fantasy': {
        'title': '星尘法师',
        'setting': '失落的大陆 - 艾瑟兰',
        'protagonist': '艾莉娅',
        'conflict': '远古魔法的复苏',
        'themes': ['命运与选择', '光明与黑暗的平衡', '传承与革新']
    },
    'thriller': {
        'title': '午夜来电',
        'setting': '现代都市',
        'protagonist': '陈默',
        'conflict': '连环谜案',
        'themes': ['真相与谎言', '正义的代价', '人性的深渊']
    }
}

def generate_novel(genre='cyberpunk', length='short', custom_prompt=''):
    """生成小说"""
    
    template = NOVEL_TEMPLATES.get(genre, NOVEL_TEMPLATES['cyberpunk'])
    
    # 字数目标
    length_targets = {'short': 1000, 'medium': 3000, 'long': 5000}
    target_words = length_targets.get(length, 1000)
    
    if custom_prompt:
        # 使用自定义提示生成
        content = generate_custom_novel(custom_prompt, target_words)
    else:
        # 使用模板生成
        content = generate_template_novel(template, target_words)
    
    return content

def generate_template_novel(template, target_words):
    """基于模板生成小说"""
    
    if template['title'] == '霓虹深渊':
        content = """# 《霓虹深渊》

## 赛博朋克短篇小说

---

公元 2147 年，新上海。

林夜站在「天穹塔」第 308 层的边缘，俯瞰着脚下这片永不沉睡的钢铁丛林。霓虹灯海在酸雨雾霭中漾开，青色、洋红、电紫的光晕交织成一张巨大的网，笼罩着这座拥有三千万人口的特大都市。

他的左眼是军用级义眼，能看见普通人看不见的东西——数据流。此刻，无数信息在他视网膜上 cascading：空中轨道列车的运行轨迹、无人机配送路径、黑市交易信号、企业安保系统的盲区……

「夜，目标出现了。」耳蜗里的 AI 助手小声提醒。

三百米外，一架黑色穿梭机正悄然降落在「神经科技」公司的私人停机坪。那是公司 CEO 陈天明的座驾。

林夜深吸一口气，纳米纤维作战服贴合着他的身体，开始调节体温。今晚，他要潜入这座守卫最森严的建筑，偷取「意识上传」项目的核心数据。

不是为了钱，是为了他妹妹。

三年前，妹妹林晓作为神经科技的初级研究员，在一次「意外」后陷入了脑死亡。公司说她签了实验协议，意识已经被上传到云端——但那是谎言。林夜查到了真相：她的意识被囚禁在公司的服务器里，成为永生项目的测试品。

「义体同调率 98.7%，可以开始了。」

林夜纵身一跃。

磁性手套和靴子让他像蜘蛛一样攀附在玻璃幕墙上。雨水顺着他的面罩滑落，折射出下方街道上全息广告牌的光芒——一个虚拟偶像正在推广最新的记忆增强芯片，笑容完美得不真实。

32 层。安保无人机巡逻间隙 6.3 秒。

他破窗而入，滚入走廊，无声落地。红外感应器被他用便携式干扰器瘫痪。走廊尽头，两个武装守卫正在交谈。

「听说了吗？7 号实验体又有反应了。」

「不可能，那项目都停了……」

林夜的瞳孔收缩。7 号——那是妹妹的编号。

他沿着通风管道爬行，义眼破解了一道又一道电子锁。数据中心在大楼地下 33 层，那里存放着公司的所有秘密。

电梯井。绳索下滑。-33 层。

指纹锁、视网膜扫描、DNA 验证——在他的军用级义体面前形同虚设。大门开启的瞬间，他看见了那个巨大的圆柱形服务器阵列，幽蓝色的指示灯如星辰般闪烁。

中央控制台上，一个全息投影正在缓缓旋转。

那是一个女孩的形象。

「哥哥？」声音从四面八方传来，带着电子合成的颤音。

林夜的眼眶湿润了。「晓……是我。我来带你走。」

「走不了。」女孩苦笑着说，「我的意识已经被分割成七万三千个数据块，分散在公司的全球服务器里。你带不走我的。」

「那就毁了它们。」林夜将数据窃取装置插入主控端口，「至少让你的意识解脱。」

「不！」林晓的投影突然变得激动，「如果服务器被毁，我就真的消失了。但现在……我至少还活着，以某种形式。」

林夜的手指悬在自毁按钮上，微微颤抖。

警报声突然响起。红色的应急灯光开始旋转。

「他们发现你了！」林晓喊道，「快走，哥哥！」

「不，我们一起走。」林夜疯狂地敲打着键盘，试图找到备份意识的方案。

「来不及了。听着——公司高层计划在明年启动『永生计划』，会把一万名富豪的意识上传……但那不是永生，是奴役。他们会成为公司的数字傀儡。」林晓的数据流开始紊乱，「你必须阻止他们……」

「晓！」

「我在云端，哥哥。只要你联网，就能看见我。去找『数字自由阵线』……他们会帮你……」

投影闪烁了几下，消失了。

林夜看着手中已经下载了 73% 的数据芯片，咬牙拔下装置。服务器阵列已经开始自锁，他必须在安保部队赶到前逃离。

他转身冲向电梯井，身后传来急促的脚步声和枪声。

子弹擦过他的肩膀，火花四溅。

攀爬。破窗。酸雨。霓虹。

当他终于回到天穹塔顶端时，整座城市依旧灯火辉煌，仿佛什么都没发生。无人机群正在封锁大厦，探照灯划破夜空。

林夜靠在冰冷的 parapet 上，看着数据芯片上的进度条——73%。

「等我，晓。」他轻声说，「我会找到完整的你。」

远处，一块巨大的全息广告牌亮起，上面是一个微笑着的虚拟女孩——那是神经科技的新代言人。

但林夜的义眼看见了隐藏在水印里的编码。

那是妹妹的信号。

她还在。在每一个像素里，在每一串数据流里，在这座赛博城市的霓虹深渊里。

而他，将是把她带回家的人。

---

**【完】**

*字数：约 1,100 字*
*创作时间：{date}*
""".format(date=datetime.now().strftime('%Y 年 %m 月 %d 日'))
    
    else:
        content = f"""# 《{template['title']}》

## {genre.capitalize()} 短篇小说

---

**设定：** {template['setting']}

**主角：** {template['protagonist']}

**核心冲突：** {template['conflict']}

**主题：** {', '.join(template['themes'])}

---

（这是一个模板故事。使用 --prompt 参数提供自定义故事大纲，或扩展此模板生成完整内容。）

---

**【完】**

*创作时间：{date}*
""".format(date=datetime.now().strftime('%Y 年 %m 月 %d 日'))
    
    return content

def generate_custom_novel(prompt, target_words):
    """根据自定义提示生成小说"""
    # 这里是简化版本，实际可以接入 AI 模型
    content = f"""# 自定义小说

## 基于提示生成

**提示：** {prompt}

---

（此处将根据 AI 模型生成完整小说内容）

---

**【完】**
"""
    return content


# ============== 动画生成模块 ==============

def generate_animation(genre='cyberpunk', output_format='both'):
    """生成动画"""
    
    print("🎬 正在生成动画...")
    
    # 导入 matplotlib
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib.patches import Rectangle
    from matplotlib.animation import FuncAnimation
    import matplotlib.patches as patches
    import random
    
    # 配色方案
    STYLE_CONFIGS = {
        'cyberpunk': {
            'background': '#0a0a12',
            'neon_cyan': '#00ffff',
            'neon_pink': '#ff00ff',
            'neon_purple': '#9d00ff',
            'building_dark': '#1a1a2e',
            'building_mid': '#16213e',
            'window_yellow': '#ffcc00',
            'window_blue': '#00ccff',
            'rain': '#a0a0ff'
        },
        'fantasy': {
            'background': '#0d0d1a',
            'neon_cyan': '#00ffff',
            'neon_pink': '#ff69b4',
            'neon_purple': '#9370db',
            'building_dark': '#1a1a2e',
            'building_mid': '#2d2d44',
            'window_yellow': '#ffd700',
            'window_blue': '#87ceeb',
            'rain': '#e6e6fa'
        },
        'thriller': {
            'background': '#050505',
            'neon_cyan': '#00ced1',
            'neon_pink': '#dc143c',
            'neon_purple': '#4b0082',
            'building_dark': '#0a0a0a',
            'building_mid': '#141414',
            'window_yellow': '#8b0000',
            'window_blue': '#191970',
            'rain': '#696969'
        }
    }
    
    colors = STYLE_CONFIGS.get(genre, STYLE_CONFIGS['cyberpunk'])
    
    # 创建画布
    fig, ax = plt.subplots(figsize=(16, 9), facecolor=colors['background'])
    ax.set_facecolor(colors['background'])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 56.25)
    ax.axis('off')
    
    buildings = []
    windows = []
    neon_signs = []
    rain_drops = []
    flying_cars = []
    data_streams = []
    
    # 创建城市
    num_buildings = 25
    x_positions = np.linspace(0, 100, num_buildings)
    
    for i, x in enumerate(x_positions):
        if i == 12:
            height = random.uniform(45, 52)
            width = random.uniform(6, 8)
        else:
            height = random.uniform(15, 35)
            width = random.uniform(3, 6)
        
        building_x = x - width / 2
        
        building = Rectangle(
            (building_x, 0),
            width,
            height,
            facecolor=colors['building_dark'] if i % 2 == 0 else colors['building_mid'],
            edgecolor=colors['neon_purple'],
            linewidth=0.5,
            alpha=0.9
        )
        ax.add_patch(building)
        buildings.append(building)
        
        # 添加窗户
        num_windows_x = int(width * 1.5)
        num_windows_y = int(height * 2)
        
        for wy in range(num_windows_y):
            for wx in range(num_windows_x):
                if random.random() > 0.6:
                    win_x = building_x + wx * (width / num_windows_x) + 0.2
                    win_y = wy * (height / num_windows_y) + 0.3
                    win_color = random.choice([colors['window_yellow'], colors['window_blue'], colors['neon_cyan']])
                    
                    window = Rectangle(
                        (win_x, win_y),
                        width / num_windows_x - 0.4,
                        height / num_windows_y - 0.6,
                        color=win_color,
                        alpha=random.uniform(0.3, 0.8)
                    )
                    ax.add_patch(window)
                    windows.append(window)
        
        # 添加霓虹灯
        if i % 3 == 0:
            neon_y = random.uniform(height * 0.3, height * 0.8)
            neon = Rectangle(
                (building_x - 0.5, neon_y),
                width + 1,
                0.3,
                color=random.choice([colors['neon_cyan'], colors['neon_pink'], colors['neon_purple']]),
                alpha=0.8
            )
            ax.add_patch(neon)
            neon_signs.append(neon)
    
    # 创建雨滴
    for _ in range(200):
        drop_x = random.uniform(0, 100)
        drop_y = random.uniform(0, 56.25)
        drop_length = random.uniform(1, 3)
        
        line = ax.plot(
            [drop_x, drop_x],
            [drop_y, drop_y - drop_length],
            color=colors['rain'],
            linewidth=0.3,
            alpha=0.4
        )[0]
        rain_drops.append({
            'line': line,
            'x': drop_x,
            'y': drop_y,
            'speed': random.uniform(0.5, 1.5),
            'length': drop_length
        })
    
    # 创建飞行汽车
    for _ in range(5):
        car_y = random.uniform(20, 50)
        car_x = random.uniform(-10, 110)
        speed = random.uniform(0.3, 0.8)
        direction = random.choice([-1, 1])
        
        car_body = patches.FancyBboxPatch(
            (car_x, car_y),
            3, 0.8,
            boxstyle="round,pad=-0.02,rounding_size=0.3",
            color=colors['neon_cyan'] if direction == 1 else colors['neon_pink'],
            alpha=0.7
        )
        ax.add_patch(car_body)
        
        trail = ax.plot(
            [car_x, car_x - direction * 2],
            [car_y + 0.4, car_y + 0.4],
            color=colors['neon_cyan'] if direction == 1 else colors['neon_pink'],
            linewidth=2,
            alpha=0.3
        )[0]
        
        flying_cars.append({
            'body': car_body,
            'trail': trail,
            'x': car_x,
            'y': car_y,
            'speed': speed,
            'direction': direction
        })
    
    # 创建数据流
    for _ in range(15):
        stream_x = random.uniform(30, 70)
        stream = ax.plot(
            [stream_x, stream_x],
            [0, 40],
            color=colors['neon_cyan'],
            linewidth=0.5,
            alpha=0.3,
            linestyle='--'
        )[0]
        data_streams.append({
            'line': stream,
            'x': stream_x,
            'offset': random.uniform(0, 100)
        })
    
    # 创建标题
    title_text = '霓虹深渊' if genre == 'cyberpunk' else 'NEON ABYSS'
    title = ax.text(50, 48, title_text, fontsize=40, fontweight='bold',
                   color=colors['neon_cyan'], ha='center', va='center', alpha=0.9)
    subtitle = ax.text(50, 43, 'Cyberpunk City 2147', fontsize=16,
                      color=colors['neon_pink'], ha='center', va='center', alpha=0.8)
    
    # 动画更新函数
    def init():
        return buildings + windows + neon_signs + flying_cars + data_streams
    
    def update(frame):
        for drop in rain_drops:
            drop['y'] -= drop['speed']
            if drop['y'] < 0:
                drop['y'] = 56.25
                drop['x'] = random.uniform(0, 100)
            drop['line'].set_data([drop['x'], drop['x']], [drop['y'], drop['y'] - drop['length']])
        
        for car in flying_cars:
            car['x'] += car['speed'] * car['direction']
            if car['x'] > 110:
                car['x'] = -10
            elif car['x'] < -10:
                car['x'] = 110
            car['body'].set_x(car['x'])
            car['trail'].set_data(
                [car['x'], car['x'] - car['direction'] * 2],
                [car['y'] + 0.4, car['y'] + 0.4]
            )
        
        for stream in data_streams:
            stream['offset'] += 2
            alpha = 0.2 + 0.3 * np.sin(np.radians(stream['offset']))
            alpha = max(0.1, min(0.9, alpha))
            stream['line'].set_alpha(alpha)
        
        for neon in neon_signs:
            alpha = 0.6 + 0.4 * np.sin(np.radians(frame * 5 + hash(str(neon)) % 360))
            neon.set_alpha(alpha)
        
        for window in windows:
            if random.random() > 0.98:
                window.set_alpha(random.uniform(0.3, 0.9))
        
        return buildings + windows + neon_signs + flying_cars + data_streams + rain_drops
    
    # 创建动画
    ani = FuncAnimation(fig, update, init_func=init, frames=200, interval=50, blit=False)
    
    # 保存
    output_dir = os.path.expanduser('~/Desktop')
    base_name = '霓虹深渊_赛博朋克动画' if genre == 'cyberpunk' else f'{genre}_animation'
    
    mp4_path = os.path.join(output_dir, f'{base_name}.mp4')
    gif_path = os.path.join(output_dir, f'{base_name}.gif')
    png_path = os.path.join(output_dir, f'{base_name}_封面.png')
    
    # 尝试保存 MP4
    if output_format in ['mp4', 'both']:
        print(f"💾 保存 MP4: {mp4_path}")
        try:
            ani.save(mp4_path, writer='ffmpeg', fps=20, dpi=100, bitrate=2000)
            print("✅ MP4 保存成功！")
        except Exception as e:
            print(f"⚠️ MP4 保存失败：{e}")
    
    # 保存 GIF
    if output_format in ['gif', 'both']:
        print(f"💾 保存 GIF: {gif_path}")
        try:
            ani.save(gif_path, writer='pill', fps=15, dpi=80)
            print("✅ GIF 保存成功！")
        except Exception as e:
            print(f"⚠️ GIF 保存失败：{e}")
    
    # 保存封面
    plt.savefig(png_path, dpi=150, facecolor=colors['background'], bbox_inches='tight')
    print(f"✅ 封面已保存：{png_path}")
    
    plt.close()
    
    return {'mp4': mp4_path, 'gif': gif_path, 'png': png_path}


# ============== 主函数 ==============

def main():
    parser = argparse.ArgumentParser(description='小说与动画生成器')
    parser.add_argument('--genre', type=str, default='cyberpunk',
                       choices=['cyberpunk', 'fantasy', 'thriller'],
                       help='故事类型')
    parser.add_argument('--length', type=str, default='short',
                       choices=['short', 'medium', 'long'],
                       help='小说长度')
    parser.add_argument('--output', type=str, default='both',
                       choices=['mp4', 'gif', 'both'],
                       help='动画输出格式')
    parser.add_argument('--prompt', type=str, default='',
                       help='自定义故事提示')
    
    args = parser.parse_args()
    
    # 生成小说
    print("📝 正在创作小说...")
    novel_content = generate_novel(args.genre, args.length, args.prompt)
    
    # 保存小说
    output_dir = os.path.expanduser('~/Desktop')
    novel_filename = '霓虹深渊_赛博朋克小说.md' if args.genre == 'cyberpunk' else f'{args.genre}_novel.md'
    novel_path = os.path.join(output_dir, novel_filename)
    
    with open(novel_path, 'w', encoding='utf-8') as f:
        f.write(novel_content)
    
    print(f"✅ 小说已保存：{novel_path}")
    print("")
    
    # 生成动画
    animation_paths = generate_animation(args.genre, args.output)
    
    print("")
    print("🎉 全部完成！")
    print("")
    print("📁 输出文件:")
    print(f"   📖 小说：{novel_path}")
    if args.output in ['mp4', 'both']:
        print(f"   🎬 动画 (MP4): {animation_paths['mp4']}")
    if args.output in ['gif', 'both']:
        print(f"   🎬 动画 (GIF): {animation_paths['gif']}")
    print(f"   🖼️ 封面：{animation_paths['png']}")


if __name__ == '__main__':
    main()