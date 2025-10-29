"""
双视频播放器 - Android版本 (Kivy)
基于原PyQt5版本改造
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.video import Video
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.properties import NumericProperty, StringProperty, BooleanProperty
import os


class VideoPlayerWidget(FloatLayout):
    """单个视频播放器组件"""
    
    current_frame = NumericProperty(0)
    total_frames = NumericProperty(0)
    is_playing = BooleanProperty(False)
    playback_speed = NumericProperty(1.0)
    video_path = StringProperty('')
    
    def __init__(self, video_num=1, **kwargs):
        super().__init__(**kwargs)
        self.video_num = video_num
        self.size_hint = (1, 1)
        
        # 创建视频组件
        self.video = Video(
            size_hint=(1, 0.85),
            pos_hint={'x': 0, 'top': 1},
            state='stop',
            options={'eos': 'loop'}
        )
        self.add_widget(self.video)
        
        # 创建信息标签
        self.info_label = Label(
            text=f'视频{video_num}: 未加载',
            size_hint=(1, 0.05),
            pos_hint={'x': 0, 'y': 0.1},
            color=(1, 1, 1, 1)
        )
        self.add_widget(self.info_label)
        
        # 创建进度条
        self.progress_slider = Slider(
            min=0,
            max=100,
            value=0,
            size_hint=(1, 0.05),
            pos_hint={'x': 0, 'y': 0.05}
        )
        self.progress_slider.bind(value=self.on_slider_change)
        self.add_widget(self.progress_slider)
        
        # 创建时间标签
        self.time_label = Label(
            text='00:00 / 00:00',
            size_hint=(1, 0.05),
            pos_hint={'x': 0, 'y': 0},
            color=(1, 1, 1, 1)
        )
        self.add_widget(self.time_label)
        
        # 定时更新
        Clock.schedule_interval(self.update_info, 0.1)
    
    def load_video(self, filepath):
        """加载视频文件"""
        if os.path.exists(filepath):
            self.video_path = filepath
            self.video.source = filepath
            self.video.state = 'stop'
            self.total_frames = int(self.video.duration * 30)  # 假设30fps
            self.info_label.text = f'视频{self.video_num}: {os.path.basename(filepath)}'
            self.update_info(0)
    
    def play(self):
        """播放视频"""
        if self.video.source:
            self.video.state = 'play'
            self.is_playing = True
    
    def pause(self):
        """暂停视频"""
        self.video.state = 'pause'
        self.is_playing = False
    
    def stop(self):
        """停止视频"""
        self.video.state = 'stop'
        self.is_playing = False
        self.video.position = 0
    
    def seek(self, position):
        """跳转到指定位置（秒）"""
        if self.video.source and self.video.duration > 0:
            self.video.seek(position / self.video.duration)
    
    def step_frame(self, frames):
        """步进指定帧数"""
        if self.video.source and self.video.duration > 0:
            fps = 30  # 假设30fps
            current_time = self.video.position * self.video.duration
            new_time = max(0, min(self.video.duration, current_time + frames / fps))
            self.seek(new_time)
    
    def on_slider_change(self, instance, value):
        """进度条改变时的处理"""
        if self.video.source and self.video.duration > 0:
            new_position = value / 100.0
            self.video.seek(new_position)
    
    def update_info(self, dt):
        """更新信息显示"""
        if self.video.source and self.video.duration > 0:
            current_time = self.video.position * self.video.duration
            total_time = self.video.duration
            
            # 更新进度条
            self.progress_slider.value = self.video.position * 100
            
            # 更新时间显示
            self.time_label.text = f'{self.format_time(current_time)} / {self.format_time(total_time)}'
            
            # 更新当前帧
            self.current_frame = int(current_time * 30)  # 假设30fps
    
    def format_time(self, seconds):
        """格式化时间显示"""
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f'{minutes:02d}:{secs:02d}'


class ControlPanel(BoxLayout):
    """控制面板"""
    
    def __init__(self, app_instance, **kwargs):
        super().__init__(**kwargs)
        self.app = app_instance
        self.orientation = 'vertical'
        self.size_hint = (1, 0.3)
        self.spacing = 5
        self.padding = 10
        
        # 播放控制按钮行
        play_row = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=5)
        
        self.play_btn = Button(
            text='播放',
            background_color=(0, 1, 0, 1),
            on_press=self.app.play_videos
        )
        play_row.add_widget(self.play_btn)
        
        self.pause_btn = Button(
            text='暂停',
            background_color=(1, 1, 0, 1),
            on_press=self.app.pause_videos
        )
        play_row.add_widget(self.pause_btn)
        
        self.stop_btn = Button(
            text='停止',
            background_color=(1, 0, 0, 1),
            on_press=self.app.stop_videos
        )
        play_row.add_widget(self.stop_btn)
        
        self.add_widget(play_row)
        
        # 加载视频按钮行
        load_row = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=5)
        
        load_video1_btn = Button(
            text='加载视频1',
            on_press=lambda x: self.app.show_file_chooser(1)
        )
        load_row.add_widget(load_video1_btn)
        
        load_video2_btn = Button(
            text='加载视频2',
            on_press=lambda x: self.app.show_file_chooser(2)
        )
        load_row.add_widget(load_video2_btn)
        
        self.add_widget(load_row)
        
        # 步进控制行
        step_row = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=5)
        
        step_row.add_widget(Label(text='步进帧数:', size_hint=(0.3, 1)))
        
        self.step_spinner = Spinner(
            text='1',
            values=[str(i) for i in [1, 5, 10, 30, 60, 100]],
            size_hint=(0.3, 1)
        )
        step_row.add_widget(self.step_spinner)
        
        backward_btn = Button(
            text='← 后退',
            on_press=lambda x: self.app.step_frames(-int(self.step_spinner.text))
        )
        step_row.add_widget(backward_btn)
        
        forward_btn = Button(
            text='前进 →',
            on_press=lambda x: self.app.step_frames(int(self.step_spinner.text))
        )
        step_row.add_widget(forward_btn)
        
        self.add_widget(step_row)
        
        # 速度控制行
        speed_row = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=5)
        
        speed_row.add_widget(Label(text='播放速度:', size_hint=(0.3, 1)))
        
        self.speed_spinner = Spinner(
            text='1.0x',
            values=['0.25x', '0.5x', '0.75x', '1.0x', '1.5x', '2.0x', '3.0x', '4.0x'],
            size_hint=(0.3, 1)
        )
        self.speed_spinner.bind(text=self.on_speed_change)
        step_row.add_widget(self.speed_spinner)
        
        self.add_widget(speed_row)
        
        # 当前视频选择行
        video_row = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=5)
        
        video_row.add_widget(Label(text='控制视频:', size_hint=(0.3, 1)))
        
        self.video_selector = Spinner(
            text='视频1',
            values=['视频1', '视频2', '两个视频'],
            size_hint=(0.7, 1)
        )
        video_row.add_widget(self.video_selector)
        
        self.add_widget(video_row)
    
    def on_speed_change(self, instance, value):
        """速度改变时的处理"""
        speed = float(value.replace('x', ''))
        self.app.set_playback_speed(speed)


class DualVideoPlayerApp(App):
    """双视频播放器主应用"""
    
    def build(self):
        # 主布局
        self.root_layout = BoxLayout(orientation='vertical')
        
        # 视频显示区域
        video_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.7))
        
        # 创建两个视频播放器
        self.player1 = VideoPlayerWidget(video_num=1)
        self.player2 = VideoPlayerWidget(video_num=2)
        
        video_layout.add_widget(self.player1)
        video_layout.add_widget(self.player2)
        
        self.root_layout.add_widget(video_layout)
        
        # 控制面板
        self.control_panel = ControlPanel(app_instance=self)
        self.root_layout.add_widget(self.control_panel)
        
        # 绑定键盘事件
        Window.bind(on_keyboard=self.on_keyboard)
        
        return self.root_layout
    
    def play_videos(self, instance=None):
        """播放视频"""
        selector = self.control_panel.video_selector.text
        if selector == '视频1' or selector == '两个视频':
            self.player1.play()
        if selector == '视频2' or selector == '两个视频':
            self.player2.play()
    
    def pause_videos(self, instance=None):
        """暂停视频"""
        selector = self.control_panel.video_selector.text
        if selector == '视频1' or selector == '两个视频':
            self.player1.pause()
        if selector == '视频2' or selector == '两个视频':
            self.player2.pause()
    
    def stop_videos(self, instance=None):
        """停止视频"""
        selector = self.control_panel.video_selector.text
        if selector == '视频1' or selector == '两个视频':
            self.player1.stop()
        if selector == '视频2' or selector == '两个视频':
            self.player2.stop()
    
    def step_frames(self, frames):
        """步进指定帧数"""
        selector = self.control_panel.video_selector.text
        if selector == '视频1' or selector == '两个视频':
            self.player1.step_frame(frames)
        if selector == '视频2' or selector == '两个视频':
            self.player2.step_frame(frames)
    
    def set_playback_speed(self, speed):
        """设置播放速度"""
        selector = self.control_panel.video_selector.text
        if selector == '视频1' or selector == '两个视频':
            self.player1.playback_speed = speed
        if selector == '视频2' or selector == '两个视频':
            self.player2.playback_speed = speed
    
    def show_file_chooser(self, video_num):
        """显示文件选择器"""
        content = BoxLayout(orientation='vertical')
        
        # 文件选择器
        filechooser = FileChooserListView(
            path='/sdcard/',
            filters=['*.mp4', '*.avi', '*.mkv', '*.mov']
        )
        content.add_widget(filechooser)
        
        # 按钮行
        button_layout = BoxLayout(size_hint=(1, 0.1), spacing=10)
        
        select_btn = Button(text='选择')
        cancel_btn = Button(text='取消')
        
        button_layout.add_widget(select_btn)
        button_layout.add_widget(cancel_btn)
        content.add_widget(button_layout)
        
        # 创建弹窗
        popup = Popup(
            title=f'选择视频{video_num}',
            content=content,
            size_hint=(0.9, 0.9)
        )
        
        def on_select(instance):
            if filechooser.selection:
                filepath = filechooser.selection[0]
                if video_num == 1:
                    self.player1.load_video(filepath)
                else:
                    self.player2.load_video(filepath)
                popup.dismiss()
        
        select_btn.bind(on_press=on_select)
        cancel_btn.bind(on_press=popup.dismiss)
        
        popup.open()
    
    def on_keyboard(self, window, key, scancode, codepoint, modifier):
        """键盘事件处理"""
        # 空格键：播放/暂停
        if key == 32:  # Space
            if self.player1.is_playing or self.player2.is_playing:
                self.pause_videos()
            else:
                self.play_videos()
            return True
        
        # 左右方向键：步进
        if key == 275:  # Right arrow
            self.step_frames(int(self.control_panel.step_spinner.text))
            return True
        elif key == 276:  # Left arrow
            self.step_frames(-int(self.control_panel.step_spinner.text))
            return True
        
        return False


if __name__ == '__main__':
    DualVideoPlayerApp().run()
