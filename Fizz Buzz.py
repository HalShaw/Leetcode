class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lst=[i for i in xrange(1,n+1)]
        for i,x in enumerate(lst):
            if type(x)==int:
                if x%3==0 and x%5==0:
                    lst[i]="FizzBuzz"
            else:
                continue        
        for i,x in enumerate(lst):
            if type(x)==int:
                if x%3==0 :
                    lst[i]="Fizz"
            else:
                continue    
        for i,x in enumerate(lst):
            if type(x)==int:
                if x%5==0:
                    lst[i]="Buzz"
            else:
                continue

        return [str(x) for x in lst]
        #一行版
        return [str(i) if (i%3!=0 and i%5!=0) else (('Fizz'*(i%3==0)) + ('Buzz'*(i%5==0))) for i in range(1,n+1)]