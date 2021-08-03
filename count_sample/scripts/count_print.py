#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 必要なライブラリをインポート
import rospy
from std_msgs.msg import Int32

# カウントした数字をサブスクライブするクラス
class CountSub():
    def __init__(self):
        # サブスクライバーを定義
        rospy.Subscriber("/count", Int32, self.callback)
        
    def callback(self, msg):
        """
        カウントされた数字を取得して表示する関数
        """

        rospy.loginfo(msg.data)

if __name__ == '__main__':
    # ノードを宣言
    rospy.init_node('count_print')
    # クラスのインスタンスを作成
    cs = CountSub()
    rate = rospy.Rate(10)
    # ループ処理開始
    while not rospy.is_shutdown():
        rate.sleep()
