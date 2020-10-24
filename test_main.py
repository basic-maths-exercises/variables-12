import numpy as np
import unittest
import main

class UnitTests(unittest.TestCase) :
    def test_fib(self) : 
       self.assertTrue( fibonacci[0]==1 and fibonacci[1]==1, "One or more of the elements in your Fibonacci array are set to the wrong value" )
       for i in range(2,100) :
           vv = fibonacci[i-2] + fibonacci[i-1]
           self.assertTrue( fibonacci[i]==vv, "One or more of the elements in your Fibonacci array are set to the wrong value" )
           
    def test_fib_length(self):
       self.assertTrue( len(fibonacci)==100, "The fibonacci array does not have a length of 100" )
       
    def test_fib_exists(self):
       self.assertTrue( "fibonacci" in globals(), "I could not find an array called fibonacci in your program" )
