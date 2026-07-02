#!/usr/bin/env python3
"""
赛博朋克风格动画生成器
为《霓虹深渊》小说制作配套动画
输出：MP4 格式
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches
from matplotlib.collections import LineCollection
import random

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 赛博朋克配色
COLORS = {
    'background': '#0a0a12',
    'neon_cyan': '#00ffff',
    'neon_pink': '#ff00ff',
    'neon_purple': '#9d00ff',
    'neon_blue': '#0066ff',
    'building_dark': '#1a1a2e',
    'building_mid': '#16213e',
    'window_yellow': '#ffcc00',
    'window_blue': '#00ccff',
    'rain': '#a0a0ff'
}

# 创建画布
fig, ax = plt.subplots(figsize=(16, 9), facecolor=COLORS['background'])
ax.set_facecolor(COLORS['background'])
ax.set_xlim(0, 100)
ax.set_ylim(0, 56.25)  # 16:9 比例
ax.axis('off')

# 存储图形元素
buildings = []
windows = []
neon_signs = []
rain_drops = []
flying_cars = []
data_streams = []

def create_cityscape():
    """创建未来城市天际线"""
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
            facecolor=COLORS['building_dark'] if i % 2 == 0 else COLORS['building_mid'],
            edgecolor=COLORS['neon_purple'],
            linewidth=0.5,
            alpha=0.9
        )
        ax.add_patch(building)
        buildings.append(building)
        
        num_windows_x = int(width * 1.5)
        num_windows_y = int(height * 2)
        
        for wy in range(num_windows_y):
            for wx in range(num_windows_x):
                if random.random() > 0.6:
                    win_x = building_x + wx * (width / num_windows_x) + 0.2
                    win_y = wy * (height / num_windows_y) + 0.3
                    win_color = random.choice([COLORS['window_yellow'], COLORS['window_blue'], COLORS['neon_cyan']])
                    
                    window = Rectangle(
                        (win_x, win_y),
                        width / num_windows_x - 0.4,
                        height / num_windows_y - 0.6,
                        color=win_color,
                        alpha=random.uniform(0.3, 0.8)
                    )
                    ax.add_patch(window)
                    windows.append(window)
        
        if i % 3 == 0:
            neon_y = random.uniform(height * 0.3, height * 0.8)
            neon = Rectangle(
                (building_x - 0.5, neon_y),
                width + 1,
                0.3,
                color=random.choice([COLORS['neon_cyan'], COLORS['neon_pink'], COLORS['neon_purple']]),
                alpha=0.8
            )
            ax.add_patch(neon)
            neon_signs.append(neon)

def create_rain():
    """创建雨滴"""
    for _ in range(200):
        drop_x = random.uniform(0, 100)
        drop_y = random.uniform(0, 56.25)
        drop_length = random.uniform(1, 3)
        
        line = ax.plot(
            [drop_x, drop_x],
            [drop_y, drop_y - drop_length],
            color=COLORS['rain'],
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

def create_flying_cars():
    """创建飞行汽车"""
    for _ in range(5):
        car_y = random.uniform(20, 50)
        car_x = random.uniform(-10, 110)
        speed = random.uniform(0.3, 0.8)
        direction = random.choice([-1, 1])
        
        car_body = patches.FancyBboxPatch(
            (car_x, car_y),
            3, 0.8,
            boxstyle="round,pad=-0.02,rounding_size=0.3",
            color=COLORS['neon_cyan'] if direction == 1 else COLORS['neon_pink'],
            alpha=0.7
        )
        ax.add_patch(car_body)
        
        trail = ax.plot(
            [car_x, car_x - direction * 2],
            [car_y + 0.4, car_y + 0.4],
            color=COLORS['neon_cyan'] if direction == 1 else COLORS['neon_pink'],
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

def create_data_streams():
    """创建数据流效果"""
    for _ in range(15):
        stream_x = random.uniform(30, 70)
        stream = ax.plot(
            [stream_x, stream_x],
            [0, 40],
            color=COLORS['neon_cyan'],
            linewidth=0.5,
            alpha=0.3,
            linestyle='--'
        )[0]
        data_streams.append({
            'line': stream,
            'x': stream_x,
            'offset': random.uniform(0, 100)
        })

def create_title():
    """创建标题"""
    title = ax.text(
        50, 48,
        'NEON ABYSS',
        fontsize=40,
        fontweight='bold',
        color=COLORS['neon_cyan'],
        ha='center',
        va='center',
        alpha=0.9
    )
    
    subtitle = ax.text(
        50, 43,
        'Cyberpunk City 2147',
        fontsize=16,
        color=COLORS['neon_pink'],
        ha='center',
        va='center',
        alpha=0.8
    )
    
    return title, subtitle

def init():
    """初始化动画"""
    return buildings + windows + neon_signs + flying_cars + data_streams

def update(frame):
    """动画更新函数"""
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
        alpha = max(0.1, min(0.9, alpha))  # 确保在 0-1 范围内
        stream['line'].set_alpha(alpha)
    
    for neon in neon_signs:
        alpha = 0.6 + 0.4 * np.sin(np.radians(frame * 5 + hash(str(neon)) % 360))
        neon.set_alpha(alpha)
    
    for window in windows:
        if random.random() > 0.98:
            window.set_alpha(random.uniform(0.3, 0.9))
    
    return buildings + windows + neon_signs + flying_cars + data_streams + rain_drops

print("🎬 正在生成赛博朋克动画...")
print("📍 创建城市天际线...")
create_cityscape()

print("🌧️  添加雨滴效果...")
create_rain()

print("🚁 添加飞行汽车...")
create_flying_cars()

print("💾 添加数据流效果...")
create_data_streams()

print("📝 添加标题...")
create_title()

print("🎞️  渲染动画中...")

ani = FuncAnimation(
    fig,
    update,
    init_func=init,
    frames=200,
    interval=50,
    blit=False
)

# 保存为 MP4 使用 ffmpeg
output_mp4 = '/home/junsheng/Desktop/霓虹深渊_赛博朋克动画.mp4'
output_gif = '/home/junsheng/Desktop/霓虹深渊_赛博朋克动画.gif'

print(f"💾 尝试保存为 MP4: {output_mp4}")

try:
    ani.save(output_mp4, writer='ffmpeg', fps=20, dpi=100, bitrate=2000)
    print("✅ MP4 动画保存成功！")
except Exception as e:
    print(f"⚠️ MP4 保存遇到问题：{e}")
    print(f"🔄 保存为 GIF: {output_gif}")
    try:
        ani.save(output_gif, writer='pill', fps=15, dpi=80)
        print("✅ GIF 动画保存成功！")
    except Exception as e2:
        print(f"⚠️ GIF 保存也遇到问题：{e2}")
        # 最后方案：保存为一帧静态图片
        print("📷 保存为静态图片作为备选...")
        plt.savefig('/home/junsheng/Desktop/霓虹深渊_赛博朋克封面.png', 
                   dpi=150, facecolor=COLORS['background'], 
                   bbox_inches='tight')
        print("✅ 封面图片已保存！")

plt.close()
print("\n🎉 完成！")