# SYMON KIMITEI
# Sigma notation and Python looping structures
# Question: Find Sigma(i+10, i=1 to i=4)
# Note: range(1,5) yields the numbers 1, 2, 3, 4
# Goal: Find the sum of (1+10)+(2+10)+(3+10)+(4+10)
#==================================================
# 1st Solution: Apply the for looping structure

sum_i = 0
for i in range (1,5):
    sum_i = sum_i + (i+10)
    
print ("(1+10)+(2+10)+(3+10)+(4+10)=",sum_i)    



    


# In[ ]:





# In[57]:


# Question: Find Sigma(i+10, i=1 to i=4)
# Goal: Find the sum of (1+10)+(2+10)+(3+10)+(4+10)
#==================================================
# 2nd Solution: Apply the while looping structure

i = 1
sum_i=0
while i <=4:
    sum_i = sum_i + (i+10)
    i = i +1
print ("(1+10)+(2+10)+(3+10)+(4+10)=",sum_i)      

    


# In[ ]:





# In[58]:



# Question: Find Sigma(i+10, i=1 to i=4)
# Goal: Find the sum of (1+10)+(2+10)+(3+10)+(4+10)
#==================================================
# 3rd Solution:Apply the Python summation function. 
# This method is tedious but simpler.

numbers = [(1+10),(2+10),(3+10),(4+10)]
print ("(1+10)+(2+10)+(3+10)+(4+10)=",sum(numbers))  



# In[ ]:





# In[ ]:





# In[59]:


# Apply the summation formula
# Question: Find Sigma(i+10, i=1 to i=4)
# Goal: Find the sum of (1+10)+(2+10)+(3+10)+(4+10)
#==================================================
# 4th Solution: Create a function that uses the summation formulas

def Sigma (n):
    return (n*(n+1)/2) + 10 *n

print ("(1+10)+(2+10)+(3+10)+(4+10)=",Sigma(4))  



# In[ ]:




