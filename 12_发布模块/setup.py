from distutils.core import setup

setup(name="zph_message",  # 包名
      version="1.0",  # 版本
      description="itzph's 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="itzph",  # 作者
      author_email="itzph@itzph.com",  # 作者邮箱
      url="www.zph.com",  # 主页
      py_modules=["zph_message.send_message",
                  "zph_message.receive_message"])