class Student:
    def __init__(self, name: str, sex: str, address: str):
        """
        :param name: 名族
        :param sex: 性别
        :param address: 地址
        """
        self.name = name
        self.sex = sex
        self.address = address

    def study(self):
        print(self.name +'在学习')

    def sleep(self):
        print(self.name + '在睡觉')


result = Student('小明', '男', '北京')
print(result.name)
print(result.sex)
print(result.address)
result.study()
result.sleep()
