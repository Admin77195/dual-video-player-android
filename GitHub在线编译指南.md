# GitHub Actions 在线编译APK指南

## 🎯 方案优势

✅ **无需本地环境** - 不需要安装WSL2  
✅ **自动化编译** - 推送代码自动编译  
✅ **快速高效** - 约20-30分钟完成  
✅ **完全免费** - GitHub Actions免费额度充足  

---

## 📋 操作步骤（5步完成）

### 第一步：创建GitHub仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - **Repository name**: `dual-video-player-android`
   - **Description**: `双视频播放器 Android版`
   - **Public** 或 **Private**（都可以）
3. 点击 **Create repository**

---

### 第二步：上传项目文件

#### 方法A：使用Git命令行（推荐）

```bash
# 1. 进入项目目录
cd D:\双视频播放器_Android

# 2. 初始化Git仓库
git init

# 3. 添加所有文件
git add .

# 4. 提交
git commit -m "Initial commit: Android version"

# 5. 关联远程仓库（替换YOUR_USERNAME为你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/dual-video-player-android.git

# 6. 推送到GitHub
git branch -M main
git push -u origin main
```

#### 方法B：使用GitHub Desktop（简单）

1. 下载并安装 GitHub Desktop: https://desktop.github.com/
2. 打开 GitHub Desktop
3. File → Add Local Repository
4. 选择 `D:\双视频播放器_Android`
5. Publish repository

#### 方法C：网页上传（最简单）

1. 在GitHub仓库页面点击 **Add file** → **Upload files**
2. 拖拽所有文件到页面
3. 点击 **Commit changes**

---

### 第三步：触发编译

上传完成后，GitHub Actions会自动开始编译！

**查看编译进度**：
1. 在GitHub仓库页面点击 **Actions** 标签
2. 查看正在运行的工作流
3. 点击进入查看详细日志

**手动触发编译**：
1. 进入 **Actions** 标签
2. 选择 **Build Android APK** 工作流
3. 点击 **Run workflow**
4. 选择 **main** 分支
5. 点击 **Run workflow** 按钮

---

### 第四步：等待编译完成

**编译时间**：约20-30分钟

**编译过程**：
1. ✓ 设置Python环境（2分钟）
2. ✓ 安装依赖包（5分钟）
3. ✓ 下载Android SDK/NDK（10分钟）
4. ✓ 编译APK（10-15分钟）
5. ✓ 上传APK（1分钟）

**查看进度**：
- 绿色勾号 ✓ = 步骤完成
- 黄色圆圈 ⚪ = 正在执行
- 红色叉号 ✗ = 执行失败

---

### 第五步：下载APK

编译成功后：

1. 在 **Actions** 页面找到完成的工作流
2. 点击进入详情页
3. 滚动到底部找到 **Artifacts** 部分
4. 点击 **android-apk** 下载
5. 解压ZIP文件，得到APK

**APK文件名**：
```
dualvideoplayer-1.4.2-arm64-v8a-debug.apk
```

---

## 📱 安装到手机

### 方法1：USB连接安装

```bash
# 1. 连接手机到电脑
# 2. 启用USB调试
# 3. 安装APK
adb install dualvideoplayer-1.4.2-arm64-v8a-debug.apk
```

### 方法2：直接传输安装

1. 将APK复制到手机
2. 在手机上打开文件管理器
3. 找到APK文件并点击安装
4. 允许安装未知来源应用

---

## 🔧 常见问题

### Q1: 编译失败怎么办？

**查看错误日志**：
1. 点击失败的工作流
2. 查看红色叉号的步骤
3. 展开查看详细错误信息

**常见错误**：

**错误1：Buildozer下载超时**
```
解决方案：重新运行工作流（通常第二次会成功）
```

**错误2：依赖安装失败**
```
解决方案：检查 requirements.txt 是否正确
```

**错误3：编译超时**
```
解决方案：GitHub Actions有6小时限制，正常情况下30分钟内完成
```

### Q2: 如何修改代码后重新编译？

```bash
# 1. 修改代码
# 2. 提交更改
git add .
git commit -m "Update code"
git push

# 3. GitHub Actions会自动重新编译
```

### Q3: 可以编译Release版本吗？

可以！修改 `.github/workflows/build.yml`：

```yaml
- name: Build APK with Buildozer
  run: |
    buildozer android release  # 改为 release
```

### Q4: 如何查看编译日志？

1. 进入 Actions 页面
2. 点击工作流
3. 点击 **build** 任务
4. 展开每个步骤查看详细日志

### Q5: APK太大怎么办？

优化方案：
1. 只编译arm64架构（已默认配置）
2. 使用Release版本（会自动压缩）
3. 移除不需要的依赖

---

## 📊 GitHub Actions配额

**免费额度**（Public仓库）：
- ✓ 无限分钟数
- ✓ 无限存储空间

**免费额度**（Private仓库）：
- ✓ 2000分钟/月
- ✓ 500MB存储空间

**本项目消耗**：
- 每次编译：约30分钟
- 每月可编译：60+次（Private仓库）

---

## 🎯 工作流配置说明

### 触发条件

```yaml
on:
  push:              # 推送代码时触发
  pull_request:      # PR时触发
  workflow_dispatch: # 手动触发
```

### 运行环境

```yaml
runs-on: ubuntu-latest  # 使用最新Ubuntu
python-version: '3.10'  # Python 3.10
```

### 编译步骤

1. **Checkout code** - 检出代码
2. **Set up Python** - 设置Python环境
3. **Install dependencies** - 安装依赖
4. **Build APK** - 编译APK
5. **Upload APK** - 上传APK

---

## 📝 项目文件清单

确保以下文件都已上传：

```
双视频播放器_Android/
├── .github/
│   └── workflows/
│       └── build.yml          ✓ GitHub Actions配置
├── main.py                    ✓ 主程序
├── buildozer.spec             ✓ 打包配置
├── requirements.txt           ✓ Python依赖
├── README.md                  ✓ 项目说明
├── 编译指南.md                 ✓ 本地编译指南
├── 快速开始.txt                ✓ 快速开始
├── 项目完成总结.md             ✓ 项目总结
├── 📱 开始阅读.txt            ✓ 入门指南
└── GitHub在线编译指南.md       ✓ 本文件
```

---

## 🚀 快速命令参考

### Git基础命令

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/dual-video-player-android.git

# 查看状态
git status

# 添加文件
git add .

# 提交
git commit -m "Your message"

# 推送
git push

# 拉取
git pull
```

### ADB命令

```bash
# 查看设备
adb devices

# 安装APK
adb install app.apk

# 卸载应用
adb uninstall com.example.app

# 查看日志
adb logcat
```

---

## 📞 需要帮助？

### GitHub相关
- GitHub文档: https://docs.github.com/
- GitHub Actions: https://docs.github.com/en/actions

### Buildozer相关
- Buildozer文档: https://buildozer.readthedocs.io/
- Python-for-android: https://python-for-android.readthedocs.io/

### 问题反馈
- 查看Actions日志
- 检查错误信息
- 搜索类似问题

---

## ✅ 完整流程检查清单

### 准备阶段
- [ ] 已有GitHub账号
- [ ] 已创建仓库
- [ ] 已安装Git（如使用命令行）

### 上传阶段
- [ ] 所有文件已上传
- [ ] .github/workflows/build.yml 存在
- [ ] buildozer.spec 配置正确
- [ ] requirements.txt 完整

### 编译阶段
- [ ] Actions已触发
- [ ] 编译正在进行
- [ ] 无错误信息
- [ ] 编译成功完成

### 测试阶段
- [ ] APK已下载
- [ ] APK已安装到手机
- [ ] 应用可以启动
- [ ] 功能正常运行

---

## 🎉 预期结果

**编译成功后**：
- ✓ APK文件大小：约20-40MB
- ✓ 支持架构：arm64-v8a, armeabi-v7a
- ✓ 最低Android版本：5.0 (API 21)
- ✓ 目标Android版本：12.0 (API 31)

**安装后**：
- ✓ 应用图标出现在桌面
- ✓ 点击启动无崩溃
- ✓ 界面显示正常
- ✓ 所有功能可用

---

**创建日期**: 2025-10-29  
**适用版本**: v1.4.2 Android  
**编译方式**: GitHub Actions  
**预计时间**: 20-30分钟

祝编译顺利！🎉
