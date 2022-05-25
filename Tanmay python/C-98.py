def countword():
    filename=input("enter the file name")
    f=open(filename)
    t=0
    for i in f:
        words=i.split()
        t=t+len(words)
    print("the file has",t,"words")
countword()
        