def amount_of_money():
    size_list = input().split()
    N = int(input())
    customer_size = []
    customer_price = []
    for _ in range(N):
        size, price = input().split()
        customer_size.append(size)
        customer_price.append(price)
    total = 0
    for i, size in enumerate(customer_size):
        if size in size_list:
            total += int(customer_price[i])
            size_list.remove(size)
    print(total)
    # print(size_list)
    # print(customer_size)
    # print(customer_price)


if __name__ == '__main__':
    shoes_amount = int(input())
    amount_of_money()
