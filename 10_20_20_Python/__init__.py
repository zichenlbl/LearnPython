# _*_coding: utf-8 _*_
# @Time    : 2020/10/20 11:25
# @Author  : zichen
"""
题目        :
设计一个Student，该类包含以下属性：id（学号）、name（姓名），
类中的方法包含计算课程的总分、平均分、最高分和等级（其中平均分在90（含）以上的A等，
80（含）-90为B等，70（含）-80为C等，60（含）-70为D等，0-60为E等）
"""


class Student:

    def __init__(self, id, name, *achievement):
        self.id = id
        self.name = name
        self.achievement = achievement
        self.输出结果()

    def 输出结果(self):
        print("id: %d, name: %s, 最高分%.1f, 平均分%.1f, 总分%.1f, 等级%s" %
              (self.getId(), self.getName(), self.最高分(), self.平均分(), self.总分(), self.等级())
              )

    def 总分(self):
        return sum(self.getAchievement())

    def 平均分(self):
        return self.总分() / len(self.getAchievement())

    def 最高分(self):
        return max(self.getAchievement())

    def 等级(self):
        if self.平均分() < 60:
            return "E"
        elif self.平均分() < 70:
            return "D"
        elif self.平均分() < 80:
            return "C"
        elif self.平均分() < 90:
            return "B"
        else:
            return "A"

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setAchievement(self, achievement):
        self.achievement = achievement

    def getAchievement(self):
        return self.achievement


student = Student(1, "jxx", 20, 20, 50)
