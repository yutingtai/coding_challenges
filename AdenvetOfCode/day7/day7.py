class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name ):
        pass


def main():
    f = open('input.txt', 'r')
    one_line_list = f.read().split('\n')


if __name__ == '__main__':
    main()
