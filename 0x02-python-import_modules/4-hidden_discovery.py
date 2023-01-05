#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *

    name_list = dir()
    for i in range(0, len(name_list)):
        if name_list[i][0:2] != "__":
            print("{}".format(name_list[i]))
