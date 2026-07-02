#!/bin/bash
# Novel Animation Generator
# 小说动画生成器 - 主执行脚本

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="$HOME/Desktop"

# 默认参数
GENRE="cyberpunk"
LENGTH="short"
OUTPUT_FORMAT="both"
CUSTOM_PROMPT=""

# 解析命令行参数
while [[ $# -gt 0 ]]; do
    case $1 in
        --genre)
            GENRE="$2"
            shift 2
            ;;
        --length)
            LENGTH="$2"
            shift 2
            ;;
        --output)
            OUTPUT_FORMAT="$2"
            shift 2
            ;;
        --prompt)
            CUSTOM_PROMPT="$2"
            shift 2
            ;;
        --help)
            echo "用法：$0 [选项]"
            echo ""
            echo "选项:"
            echo "  --genre     类型：cyberpunk|fantasy|thriller (默认：cyberpunk)"
            echo "  --length    长度：short|medium|long (默认：short)"
            echo "  --output    格式：mp4|gif|both (默认：both)"
            echo "  --prompt    自定义故事提示"
            echo "  --help      显示帮助"
            exit 0
            ;;
        *)
            echo "未知选项：$1"
            exit 1
            ;;
    esac
done

echo "======================================"
echo "  小说动画生成器 v1.0"
echo "======================================"
echo ""
echo "配置:"
echo "  - 类型：$GENRE"
echo "  - 长度：$LENGTH"
echo "  - 输出：$OUTPUT_FORMAT"
echo ""

# 检查依赖
echo "🔍 检查依赖项..."
python3 -c "import matplotlib" 2>/dev/null || {
    echo "❌ 缺少 matplotlib，正在安装..."
    pip3 install matplotlib numpy pillow --quiet
}

# 运行生成器
echo ""
echo "🚀 开始生成..."
python3 "$SCRIPT_DIR/generator.py" \
    --genre "$GENRE" \
    --length "$LENGTH" \
    --output "$OUTPUT_FORMAT" \
    --prompt "$CUSTOM_PROMPT"

echo ""
echo "======================================"
echo "  ✅ 完成！"
echo "======================================"
echo ""
echo "输出文件:"
ls -lh "$OUTPUT_DIR"/*霓虹深渊* 2>/dev/null || echo "  文件保存在：$OUTPUT_DIR"
echo ""