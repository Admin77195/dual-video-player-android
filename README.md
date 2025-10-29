# 双视频播放器 - Android版本

## 📱 项目信息

**版本**: 1.4.2 (Android)  
**基于**: PyQt5版本改造  
**框架**: Kivy  
**目标设备**: Xiaomi 15 Ultra (骁龙8至尊版)

---

## ✨ 功能特性

### 已实现功能

✅ **双视频播放**
- 同时播放两个视频
- 独立控制每个视频
- 文件选择器加载视频

✅ **播放控制**
- 播放/暂停/停止
- 进度条拖动
- 时间显示

✅ **帧精确控制**
- 前进/后退指定帧数
- 可选步进值：1, 5, 10, 30, 60, 100帧
- 键盘方向键控制

✅ **播放速度控制**
- 速度范围：0.25x - 4.0x
- 预设速度选择
- 独立或同步控制

✅ **触摸优化**
- 大按钮设计
- 触摸友好的UI
- 横屏布局

---

## 🎮 操作说明

### 按钮控制

| 按钮 | 功能 |
|------|------|
| **播放** | 播放选中的视频 |
| **暂停** | 暂停选中的视频 |
| **停止** | 停止选中的视频 |
| **加载视频1/2** | 选择并加载视频文件 |
| **← 后退** | 后退指定帧数 |
| **前进 →** | 前进指定帧数 |

### 键盘快捷键

| 按键 | 功能 |
|------|------|
| **空格** | 播放/暂停 |
| **→** | 前进N帧 |
| **←** | 后退N帧 |

### 控制选项

- **步进帧数**: 选择每次前进/后退的帧数
- **播放速度**: 选择播放速度倍率
- **控制视频**: 选择控制哪个视频（视频1/视频2/两个视频）

---

## 📦 编译说明

### 环境要求

- **操作系统**: Linux (推荐Ubuntu 22.04) 或 WSL2
- **Python**: 3.8+
- **Buildozer**: 最新版本
- **Android SDK**: API 31
- **Android NDK**: r25b

### 安装依赖

```bash
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装Python和pip
sudo apt install -y python3 python3-pip

# 安装Buildozer依赖
sudo apt install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# 安装Cython和Buildozer
pip3 install --upgrade cython==0.29.33
pip3 install buildozer
```

### 编译APK

```bash
# 进入项目目录
cd /path/to/双视频播放器_Android

# 初始化Buildozer（首次）
buildozer init

# 编译Debug版本
buildozer -v android debug

# 编译Release版本
buildozer -v android release
```

### 安装到设备

```bash
# 通过USB安装
buildozer android deploy run

# 或手动安装
adb install bin/*.apk
```

---

## 🔧 开发说明

### 项目结构

```
双视频播放器_Android/
├── main.py              # 主程序（Kivy版本）
├── buildozer.spec       # 打包配置文件
├── requirements.txt     # Python依赖
└── README.md           # 本文件
```

### 核心改动

**PyQt5 → Kivy 转换**:

| PyQt5 | Kivy |
|-------|------|
| QMainWindow | App |
| QWidget | Widget/Layout |
| QLabel | Label |
| QPushButton | Button |
| QSlider | Slider |
| QTimer | Clock |
| cv2.VideoCapture | Video |

### 简化功能

为适配移动端，以下功能已简化或移除：

❌ **已移除**:
- 滚轮缩放（触摸屏不适用）
- 连续播放（可后续添加）
- 授权系统（移动端不需要）
- 复杂的帧计数器技术

✅ **保留核心功能**:
- 双视频播放
- 帧精确控制
- 播放速度控制
- 进度条控制

---

## 📱 测试设备

**Xiaomi 15 Ultra**:
- 处理器: 骁龙8至尊版
- 内存: 16GB
- 存储: 512GB
- 屏幕: 6.73寸 3200×1440
- 系统: HyperOS 2.0

**性能预期**:
- 流畅播放1080p视频
- 双视频同时播放无压力
- 快速帧跳转响应

---

## ⚠️ 注意事项

### 权限要求

应用需要以下权限：
- **READ_EXTERNAL_STORAGE**: 读取视频文件
- **WRITE_EXTERNAL_STORAGE**: 保存设置（可选）
- **INTERNET**: 未来功能预留

### 视频格式支持

推荐格式：
- ✅ MP4 (H.264)
- ✅ AVI
- ✅ MKV
- ✅ MOV

### 性能优化建议

1. **视频分辨率**: 建议1080p或以下
2. **编码格式**: H.264性能最佳
3. **文件大小**: 单个视频建议<500MB
4. **同时播放**: 两个视频总码率建议<20Mbps

---

## 🐛 已知问题

1. **视频同步**: 两个视频可能存在轻微延迟
2. **帧精确度**: 依赖视频编码，可能不是完全精确
3. **文件选择器**: 路径可能需要根据设备调整

---

## 🔄 后续计划

### 待添加功能

- [ ] 连续播放功能
- [ ] 视频缩放功能
- [ ] 手势控制（双指缩放、滑动步进）
- [ ] 视频对比模式（上下/左右）
- [ ] 播放列表
- [ ] 视频信息显示
- [ ] 设置保存功能

### 优化计划

- [ ] 性能优化
- [ ] UI美化
- [ ] 更好的触摸体验
- [ ] 多语言支持

---

## 📞 技术支持

如有问题，请查看：
1. Kivy官方文档: https://kivy.org/doc/stable/
2. Buildozer文档: https://buildozer.readthedocs.io/
3. 原PyQt5版本代码参考

---

## 📄 版本历史

**v1.4.2 (Android)**
- 初始Android版本
- 基于PyQt5 v1.42改造
- 实现核心播放功能
- 优化移动端体验

---

## 🎯 快速开始

### Windows用户（使用WSL2）

```bash
# 1. 安装WSL2
wsl --install -d Ubuntu-22.04

# 2. 在WSL中克隆项目
cd ~
cp -r /mnt/d/双视频播放器_Android ./

# 3. 安装依赖（见上文）

# 4. 编译APK
cd ~/双视频播放器_Android
buildozer -v android debug

# 5. APK位置
# bin/dualvideoplayer-1.4.2-arm64-v8a-debug.apk
```

### Linux用户

```bash
# 1. 进入项目目录
cd /path/to/双视频播放器_Android

# 2. 安装依赖（见上文）

# 3. 编译APK
buildozer -v android debug
```

---

**开发时间**: 2025-10-29  
**状态**: 开发中  
**测试状态**: 待测试

---

*最后更新: 2025-10-29 14:04 - 触发 GitHub Actions 构建*
