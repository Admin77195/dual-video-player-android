[app]

# 应用标题
title = 双视频播放器

# 包名
package.name = dualvideoplayer

# 包域名
package.domain = org.example

# 源代码目录
source.dir = .

# 源代码包含的文件
source.include_exts = py,png,jpg,kv,atlas

# 应用版本
version = 1.4.2

# 应用要求的权限
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# 支持的架构
android.archs = arm64-v8a,armeabi-v7a

# Python依赖
requirements = python3,kivy,ffpyplayer

# 应用图标（可选）
# icon.filename = %(source.dir)s/assets/icon.png

# 启动画面（可选）
# presplash.filename = %(source.dir)s/assets/presplash.png

# Android API版本
android.api = 31
android.minapi = 21
android.ndk = 25b

# 应用方向
orientation = landscape

# 全屏模式
fullscreen = 0

# Android主题
android.theme = "@android:style/Theme.NoTitleBar"

# 日志级别
log_level = 2

# 警告忽略
warn_on_root = 1


[buildozer]

# 日志级别
log_level = 2

# 警告忽略
warn_on_root = 1
