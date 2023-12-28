def func(List,length):
    print(List[length-1], end=" ")
    func(List,length-1)
func([4,3,2,1],4)