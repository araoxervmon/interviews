def solution(x):
    output=[]
    for i in range(1, x+1):
        for j in range(1, x+1): 
            output.append(i*j)
    print(output)
if __name__=="__main__":
    x =int(input())
    solution(x)