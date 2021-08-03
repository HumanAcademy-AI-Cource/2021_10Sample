#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 必要なライブラリをインポート
import rospy
from std_msgs.msg import Int32

# 数字をカウントダウンしてパブリッシュするクラス
class CountDown():
    def __init__(self):
        # パブリッシャーを定義
        self.pub = rospy.Publisher("/count", Int32, queue_size=10)
        # カウントした値を保持する変数
        self.counter = 2021
        
    def run(self):
        """
        一連の処理を行う関数
        """

        self.pub.publish(self.counter)
        self.counter = self.counter - 1

if __name__ == '__main__':

    # ノードを宣言
    rospy.init_node('count_down')
    # クラスのインスタンスを作成
    cd = CountDown()
    # 一定周期で処理を実行するための準備
    rate = rospy.Rate(1)
    # 2秒間待つ
    print("2秒後にカウントダウン開始！")
    rospy.sleep(2.0)
    # ループ処理開始
    while not rospy.is_shutdown():
        # 処理を実行
        cd.run()
        rate.sleep()
