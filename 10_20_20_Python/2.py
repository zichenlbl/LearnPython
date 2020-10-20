# 设计一个Student，该类包含以下属性：id（学号）、name（姓
# 名），类中的方法包含计算课程的总分、平均分、最高分和等级
# （其中平均分在90（含）以上的A等，80（含）-90为B等，70（含
# ）-80为C等，60（含）-70为D等，0-60为E等）。
class Student:

    def __init__(self, id1, name, *cj):
        self.__id = id1
        self.__name = name
        self.__cj = cj
        self.输出()  # 调用函数

    def 输出(self):
        print("id: %d, name: %s, 最高分%.1f, 平均分%.1f, 总分%.1f, 等级%s" %
              (self.getId(), self.getName(), self.getZgf(), self.getPjf(), self.getZf(), self.getDj())
              )

    def getZf(self):
        return sum(self.__cj)

    def getPjf(self):
        return self.getZf() / len(self.__cj)

    def getZgf(self):
        return max(self.__cj)

    def getDj(self):
        if self.getPjf() >= 90:
            return "A"
        elif self.getPjf() >= 80:
            return "B"
        elif self.getPjf() >= 70:
            return "C"
        elif self.getPjf() >= 60:
            return "D"
        else:
            return "E"

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setId(self, id1):
        self.__id = id1

    def getId(self):
        return self.__id

    def getCj(self):
        return self.__cj

    def setCj(self, cj):
        self.__cj = cj


student = Student(1, "jxx", 20, 20, 50)
