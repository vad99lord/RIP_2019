from collections import OrderedDict


# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        if len(kwargs) > 0:
            self.ignore_case = kwargs['ignore_case']
        self.items = self.init_items(items)
        self.pos = -1

    def init_items(self, items):
        if self.ignore_case:
            od = OrderedDict((item, None) for item in items)
        else:
            od = OrderedDict()
            for item in items:
                is_found = False
                for key in od.keys():
                    if key.lower() == item.lower():
                        is_found = True
                        break
                if not is_found:
                    od[item] = None
        # convert to list for iteration
        return list(od.keys())

    def __next__(self):
        # Нужно реализовать __next__
        self.pos += 1
        if self.pos==len(self.items):
            raise StopIteration
        return self.items[self.pos]


    def __iter__(self):
        return self
