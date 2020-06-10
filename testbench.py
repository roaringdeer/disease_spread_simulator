def main():
    temp = {1: 2, 2: 3, (3, 4): 4}
    print(temp[3, 4])
    print(temp[(3, 4)])
    temp1 = {}
    for key, val in temp.items():
        temp1[key] = val
    print(temp1)


if __name__ == '__main__':
    main()
