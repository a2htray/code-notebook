# -*- coding=utf-8 -*-
r"""
1. 调用者无须了解具体的实现类
2. Creator 类提供用于创建具体类对象
"""
from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def handle(self, data):
        raise NotImplemented


class OddHandler(Handler):
    def handle(self, data):
        ret = []
        for v in data:
            if v % 2 == 1:
                ret.append(v)
        return ret


class EvenHandler(Handler):
    def handle(self, data):
        ret = []
        for v in data:
            if v % 2 == 0:
                ret.append(v)
        return ret


class HandlerCreator:
    @staticmethod
    def create_handler(typ):
        if typ == 'odd':
            return OddHandler()
        if typ == 'even':
            return EvenHandler()
        return None


if __name__ == '__main__':
    odd_handler = HandlerCreator.create_handler('odd')
    print(odd_handler.handle([1, 2, 3, 4]))

    even_handler = HandlerCreator.create_handler('even')
    print(even_handler.handle([1, 2, 3, 4]))
