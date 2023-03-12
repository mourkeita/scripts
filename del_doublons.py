#/usr/bin/python
#coding: utf8

print('Delete doublons in a list')
class Listed(list):
    def __init__(self):
        pass

    def del_doublons(self, l):
        res = []
        for i  in range(len(l)):
            if l[i] not in res:
                res.append(l[i])
        return res


if __name__ == '__main__':
    l = Listed()
    print(l.del_doublons([4, 5, 3, 2, 2, 1, 9, 90]))
