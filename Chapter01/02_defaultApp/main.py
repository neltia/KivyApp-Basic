""" main.py """

import kivy
kivy.require('1.0.6') # ﻿require로 사용 키비 버전 지정

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label(text='Hello world') # 라벨


if __name__ == '__main__':
    MyApp().run()