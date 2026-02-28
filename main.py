from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
import os

Window.fullscreen = 'auto'

class SOSApp(App):
    def build(self):
        self.layout = FloatLayout()
        self.is_active = False
        self.event = None

        self.sos_btn = Button(
            text="START SOS",
            font_size='40sp',
            size_hint=(0.6, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            background_normal='',
            background_color=(0.8, 0, 0, 1)
        )
        self.sos_btn.bind(on_press=self.start_protocol)

        self.stop_btn = Button(
            text="STOP",
            font_size='40sp',
            size_hint=(0.6, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            background_normal='',
            background_color=(0.3, 0.3, 0.3, 1),
            disabled=True
        )
        self.stop_btn.bind(on_press=self.stop_protocol)

        self.layout.add_widget(self.sos_btn)
        self.layout.add_widget(self.stop_btn)
        return self.layout

    def play_beep(self, dt):
        try:
            from jnius import autoclass
            ToneGenerator = autoclass('android.media.ToneGenerator')
            AudioManager = autoclass('android.media.AudioManager')
            tone_gen = ToneGenerator(AudioManager.STREAM_ALARM, 100)
            tone_gen.startTone(ToneGenerator.TONE_CDMA_EMERGENCY_RINGBACK, 500)
        except:
            print("\a")

    def start_protocol(self, instance):
        if not self.is_active:
            self.is_active = True
            self.sos_btn.disabled = True
            self.stop_btn.disabled = False
            self.event = Clock.schedule_interval(self.play_beep, 0.6)

    def stop_protocol(self, instance):
        if self.is_active:
            self.is_active = False
            self.sos_btn.disabled = False
            self.stop_btn.disabled = True
            if self.event:
                self.event.cancel()

if __name__ == '__main__':
    SOSApp().run()
