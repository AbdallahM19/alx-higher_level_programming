#!/usr/bin/python3
if __name__ == "__main__":
    # print all names which in hidden_4 module.
    import hidden_4
    for name in dir(hidden_4):
        if name[:2] != "__":
            print(name)
