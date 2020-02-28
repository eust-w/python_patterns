# 设计模式

## 原则

### 开闭原则

* 1. 提高扩展维护性
  2. 对扩展开放，对修改关闭，在扩展时不修改源码的一种效果
  3. 在开发时要考虑在新建子类或者新建方法时不用修改原有代码或者父类

### 代换原则

* 1. 对开闭原则的补充

  2. 父类更抽象而相应子类是对父类的具象化（具象化过程中子类将产生新的行为）
### 隔离原则

* 1. 接口细分，使用多个接口

  2. 降低耦合性

### 合成复用原则

* 1. 尽量少使用继承，尽量使用合成聚合方式。

  2. 与继承思想相反，零件组装的思想而非填空的思想

### Demeter 原则

* 1. 已经具象化的实体之间不要有耦合

  2. 模块之间尽量独立，尽量通过固定的接口进行数据的传输

### 依赖倒转原则

* 1. 针对接口编程而非具体的内容

 ## 创建型模式（ Creational Patterns ）

这些设计模式提供了一种在创建对象的同时隐藏创建逻辑的方式

### 单例模式(Singleton Patterns)

* 1. 确保一个模式只有一个实例
2. 保证一个类仅有一个实例，并提供一个访问它的全局访问点

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""@author:longt
@file:singleton.py
@time:2020/02/28
"""


class Singleton(object,):
    def __init__(self):
        self.a = self
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            # 反射
            Singleton._instance = object.__new__(cls)
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)   # <__main__.Singleton object at 0x004415F0> <__main__.Singleton object at 0x004415F0>
print(obj1 is obj2)
```



### 简单工厂模式(Simple Factory Patterns)

* 1. 对单个接口的集中管理
2. 在工厂中选择实例化哪一个类

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""@author:longt
@file:factorial.py
@time:2020/02/28
"""


class Person:
    def __init__(self):
        self.name = None
        self.gender = None

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender


class Male(Person):
    def __init__(self, name):
        print('Hello Mr.' + name)


class Female(Person):
    def __init__(self, name):
        print('Hello Miss.' + name)


class Factory:
    def get_person(self, name, gender):
        if gender == 'M':
                return Male(name)
        if gender == 'F':
            return Female(name)


if __name__ == '__main__':
    factory = Factory()
    person1 = factory.get_person("Chetan", "M")
    person2 = factory.get_person("Chetan", "M")

    print(person1 is person2)
```



### 抽象工厂模式(Abstract Factory Patterns)

* 1. 简单工厂模式的工厂

  2. 在抽象工厂中抽象出其它工厂（给不同的接口）

### 建造者模式(Builder Patterns)

* 1. 建造者：类的定义
  2. 具体建造者：类的具体内容
  3. 监工（指挥者）：类的逻辑结构
  4. 结果：多个监工的共同结果

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""@author:longt
@file:builder.py
@time:2020/02/28
"""
from abc import ABCMeta, abstractmethod


class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_left_arm(self):
        pass

    @abstractmethod
    def draw_right_arm(self):
        pass

    @abstractmethod
    def draw_left_foot(self):
        pass

    @abstractmethod
    def draw_right_foot(self):
        pass

    @abstractmethod
    def draw_head(self):
        pass

    @abstractmethod
    def draw_body(self):
        pass


class Thin(Builder):
    def draw_left_arm(self):
        print('画左手')

    def draw_right_arm(self):
        print('画右手')

    def draw_left_foot(self):
        print('画左脚')

    def draw_right_foot(self):
        print('画右脚')

    def draw_head(self):
        print('画头')

    def draw_body(self):
        print('画瘦身体')


class Fat(Builder):
    def draw_left_arm(self):
        print('画左手')

    def draw_right_arm(self):
        print('画右手')

    def draw_left_foot(self):
        print('画左脚')

    def draw_right_foot(self):
        print('画右脚')

    def draw_head(self):
        print('画头')

    def draw_body(self):
        print('画胖身体')


class Director:
    def __init__(self, person):
        self.person = person

    def draw(self):
        self.person.draw_left_arm()
        self.person.draw_right_arm()
        self.person.draw_left_foot()
        self.person.draw_right_foot()
        self.person.draw_head()
        self.person.draw_body()


if __name__ == '__main__':
    thin = Thin()
    fat = Fat()
    director_thin = Director(thin)
    director_thin.draw()
    director_fat = Director(fat)
    director_fat.draw()  
```



### 原型模式(Prototype Patterns)

## 结构性模式



## 行为型模型



