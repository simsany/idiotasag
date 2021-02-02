# import pytest
# import coverage
# class TestJojo():
  
  
    
 
  
#     testdata=[[1,2,3,'mustbe'],[3,2,1,'maybe']]
  
#     @pytest.mark.parametrize('a,b,c,exp',testdata)
 
  
#     def test_jojo(self,a,b,c,exp):
    
a=4
b=2
c=3
    
if c>a:
    b_smaller=c>b
    c_smaller=c<=b
    
    res='mustbe'*b_smaller + 'proceed'*c_smaller
    print(res)           

else:

    res='maybe'
    print(res)

if c>a:
    if c>b:
        res='mustbe'
        print(res)
    else:
        res='proceed'
        print(res)
else:
    res="maybe"
    print(res)
    

        
        
        
        
        # assert res==exp




  

