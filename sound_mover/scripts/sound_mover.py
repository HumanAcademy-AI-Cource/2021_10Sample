#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 必要なライブラリをインポート
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

import pyaudio
import audioop
import numpy as np
import math


# ロボットを動かすクラス
class SoundMover():
    def __init__(self):
        # サブスクライバーを定義
        rospy.Subscriber("/sound", Float64, self.callback)
        # パブリッシャーを定義
        self.cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

        # 速度を保持する変数
        self.cmd_vel = Twist()
        # 定速の値を定義
        self.const_vel = 0.2
        # データ保存用の変数
        self.decibel = 0

    def callback(self, msg):
        """
        受け取った音センサの値からロボットに速度指令を出す関数
        """

        self.decibel = msg.data
        # 音センサ（マイク）の値が70を超えたらタイヤを回す
        if abs(self.decibel) > 70:
            self.cmd_vel.linear.x = 1.0
            self.cmd_vel.angular.z = 0.0
        else:
            self.cmd_vel.linear.x = 0.0
            self.cmd_vel.angular.z = 0.0
        # 速度をパブリッシュ
        self.cmd_pub.publish(self.cmd_vel)


if __name__ == '__main__':

    # ノードを宣言
    rospy.init_node('sound_mover')
    # クラスのインスタンスを作成
    sm = SoundMover()
    rospy.spin()