from django.db import models
import mongoengine

# Create your models here.
'''职位'''


class Liepin(mongoengine.Document):
    # 职位
    title = mongoengine.StringField(max_length=100)
    # 工资
    pay = mongoengine.FloatField()
    # 地点
    site = mongoengine.StringField(max_length=225)
    # 发布时间
    release_time = mongoengine.DateField()
    # 招聘要求
    condition = mongoengine.StringField(max_length=225)
    # 工作经验
    work_time = mongoengine.StringField(max_length=225)


'''社区'''


class Liepin_community(mongoengine.Document):
    # 主题
    title = mongoengine.StringField(max_length=100)
    # 名字
    name1 = mongoengine.StringField(max_length=100)
    name2 = mongoengine.StringField(max_length=100)
    name3 = mongoengine.StringField(max_length=100)
    name4 = mongoengine.StringField(max_length=100)


'''海外招聘'''


class Liepin_overseas(mongoengine.Document):
    # 公司logo
    company_logo = mongoengine.ImageField()
    # 公司名
    company_title = mongoengine.StringField(max_length=100)
    # 职位一
    position1 = mongoengine.StringField(max_length=100)
    # 职位二
    position2 = mongoengine.StringField(max_length=100)


'''公司招聘详情'''


class Company_detail(mongoengine.Document):
    # 职位
    title = mongoengine.StringField(max_length=100)
    # 工资
    pay = mongoengine.FloatField()
    # 地点
    site = mongoengine.StringField(max_length=100)
    # 发布时间
    release_time = mongoengine.DateField()
    # 招聘要求
    condition = mongoengine.StringField(max_length=225)
    # 工作经验
    work_time = mongoengine.StringField(max_length=100)
