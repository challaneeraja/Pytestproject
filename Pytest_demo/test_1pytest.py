def test_demo1():
    a=10
    b=20
    assert a!=b
    print("my first pytest")
def test_demo2():
    name='HCL'
    text='HCL is located all over the world'
    assert name in text
    print("my second pytest")
