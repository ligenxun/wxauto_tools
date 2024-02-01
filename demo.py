from wxauto import WeChat

wx = WeChat()

# 发送消息
who = '文件传输助手'

# 发送剪切板上的内容（包括图片、文件、文字）
# 注意，原项目中的SendMsg可能会存在无法发送纯数字类型消息，这是win32剪切板复制的问题，而非粘贴问题，使用上述SendClipboardMsg这个直接发送剪切板上内容，是可以发送纯数字消息的。使用前自己把数字内容放到剪切板上即可。
wx.SendClipboardMsg(who)

for i in range(3):
    wx.SendMsg(f'wxauto测试{i+1}', who)
    
# 获取当前聊天页面（文件传输助手）消息，并自动保存聊天图片
msgs = wx.GetAllMessage(savepic=True)
for msg in msgs:
    print(f"{msg[0]}: {msg[1]}")


print('wxauto测试完成！')
