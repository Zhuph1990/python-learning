class MusicPlayer(object):


    def __new__(cls, *args, **kwargs):
        """
        > 重写 `__new__` 方法 的代码非常固定！
        - 重写 `__new__` 方法 **一定要** `return super().__new__(cls)`
        - 否则 Python 的解释器 **得不到** 分配了空间的 **对象引用**，**就不会调用对象的初始化方法**
        - 注意：`__new__` 是一个静态方法，在调用时需要 **主动传递** `cls` 参数
        :param args:
        :param kwargs:
        :return:
        """

        # 1.
        print("创建对象，分配内存")

        # 2. 为对象分配内存
        instance = super().__new__(cls)

        # 3. 返回对象的引用
        return instance

    def __init__(self):
        print("初始化音乐播放对象")


player = MusicPlayer()

print(player)