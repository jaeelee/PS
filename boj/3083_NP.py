if __name__ == '__main__':
    L = int(input())
    X = [ [int(i),0,0] for i in list(input().split(' ')) ]
    N = int(input())
    truck = []
    for i in range(N):
        truck.append( [ int(j) for j in list(input().split(' ')) ] )
    K = int(input())

    # print(L,X,N,truck,K)

    for i in range(N):
        if truck[i][0] > truck[i][1]:
            for j in range(truck[i][1], truck[i][0]):
                X[j][2] += 1
        else:
            for j in range(truck[i][0], truck[i][1]):
                X[j][1] += 1
    price = 0
    for i in range(N):
        if X[i][1] > K or X[i][2] > K:
            price += X[i][0]
            X[i][0] = 0

    for i in range(N):
        sum = 0
        if truck[i][0] > truck[i][1]:
            for j in range(truck[i][1], truck[i][0]):
                sum += X[j][0]
        else:
            for j in range(truck[i][0], truck[i][1]):
                sum += X[j][0]
        if sum > truck[i][2]:
            price += truck[i][2]
        else:
            price += sum
    
    print(price)