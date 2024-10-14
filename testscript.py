# this is a test commit 
def add(a,b):
    return a+b
    print("the value of sum of the numbers ",a+b)
    

def test_add():
    assert add(1,2)==3
    assert add(1,-1)==0
