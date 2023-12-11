import main

def test_Hallo1():
    assert main.Hallo() == "Hello World"
    
def test_Hallo2():
    assert main.Hallo("Otto") == "Hello Otto"    
