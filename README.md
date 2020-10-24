# The Fibonacci Series

Hopefully, you recognised that you can solve the problem in the previous exercise by writing code like that shown on the left here.  Don't worry if you didn't get to the code on the right - the tests on that last exercise are not particularly robust - as long as you understand how the code on the left works you should be fine to continue.  The point that I wanted to make in that previous exercise is that we can compute 7n by evaluating the following sum: 

![](https://render.githubusercontent.com/render/math?math=7n=\sum_{i=1}^n7)

In that last exercise, I wanted to show you how we can evaluate a sum of terms by writing a computer program containing a loop.  The reason for going through this exercise is that in the MTH1002 module you are going to spend a lot of time working with mathematical series. In this final block of exercise, I thus want to show you a few ways that you can use the Python we have covered thus far to get to grips with the series you are studying.  In this exercise, we are thus going to use what we know of Python to evaluate some of the terms in the Fibonacci series.

The 1st and 2nd term in the Fibonacci series are both 1.  All remaining terms in the Fibonacci series are evaluated using the following formula:

![](https://render.githubusercontent.com/render/math?math=f_n=f_{n-2}%2Bf_{n-1})

To complete this exercise I would thus like you to:

1. Create an array called `fibonacci`.  This array should have 100 elements.
2. Set `fibonacci[0]` and `fibonacci[1]` both equal to 1.
3. Write a for loop that uses the formula given above to evaluate set the remaining 98 elements in the array `fibonacci` 

At the end of your program the elements of `fibonacci` should be set equal to the first 100 numbers in the Fibonacci series.

***

Note: If you write:

````
for i in range(2,4) : 
    print(i) 
````

This code will output:

````
2
3
````

as the loop runs for all i in ![](https://render.githubusercontent.com/render/math?math=2\le\i<4)
