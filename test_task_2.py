import pytest
import task_2

def my_test():
    assert task_2.func() == [14, 28, 29, 35, 41, 53, 67, 76, 82, 92]
    
def my_test_2():
  lst=[]
  for i in range(10, 100):
    if function(i) % 17 == 0:
      lst.append(i)
	assert(lst == [14, 28, 29, 35, 41, 53, 67, 76, 82, 92])
