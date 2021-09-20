#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ok，音频拼接
from pydub import AudioSegment  # 先导入这个模块

# 加载需要合并的两个mp3音频
parameters = None
input_music_1 = AudioSegment.from_mp3("solongmichael1.mp3")  # 需要修改的地方：音频1
input_music_2 = AudioSegment.from_mp3("solongmichael2.mp3")
input_music_3 = AudioSegment.from_mp3("solongmichael3.mp3")
input_music_4 = AudioSegment.from_mp3("solongmichael4.mp3")
input_music_5 = AudioSegment.from_mp3("solongmichael5.mp3")
input_music_6 = AudioSegment.from_mp3("solongmichael6.mp3")# 需要修改的地方：音频2
# 获取两个音频的响度（音量）
input_music_1_db = input_music_1.dBFS
input_music_2_db = input_music_2.dBFS
input_music_3_db = input_music_3.dBFS
input_music_4_db = input_music_4.dBFS
input_music_5_db = input_music_5.dBFS
input_music_6_db = input_music_6.dBFS
# 获取两个音频的时长，单位为毫秒
input_music_1_time = len(input_music_1)
input_music_2_time = len(input_music_2)
input_music_3_time = len(input_music_3)
input_music_4_time = len(input_music_4)
input_music_5_time = len(input_music_5)
input_music_6_time = len(input_music_6)
# 调整两个音频的响度一致

# 合并音频
output_music = input_music_1 + input_music_2+input_music_3+input_music_4+input_music_5+input_music_6
# 简单输入合并之后的音频
output_music.export("solongmichaelpython.mp3", format="mp3")  # 前面是保存路径，后面是保存格式
# 复杂输入合并之后的音频
# bitrate：比特率，album：专辑名称，artist：歌手，cover：封面图片
# 需要修改的地方：输出音频。cover那个没用着，可以删掉。
output_music.export("D:/output_music.mp3", format="mp3", bitrate="192k", tags={"album": "Jerry", "artist": "Jerry"}, cover="D:/1.jpg")
print(len(output_music), output_music.channels)# 合并音频的时长，音频的声道，1是单声道，2是立体声