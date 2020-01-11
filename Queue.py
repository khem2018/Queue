#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[21]:


class Queue:
    def __init__(self, top=None, tail=None):
        self.top=top
        self.tail=tail
        self.size=0

    def enqueue(self, data):
        n1 = Node(data)
        if (self.tail==None or self.top==None):
            self.tail=n1
            self.top=n1
        else:
            self.curr = self.top
            self.top=n1
            self.top.next = self.curr
            self.curr.pre=  self.top
        self.size+=1

    def dequeue(self):
        self.pop = self.tail
        self.tail = self.tail.pre
        self.tail.next = None
        self.size-=1
        return 'Element removed {ele}'.format(ele=self.pop.data)

    def get_size(self):
        return self.size

class Node:
    def __init__(self,data ,next=None, pre=None):
        self.data=data
        self.next=next
        self.pre=pre


# In[22]:


obj= Queue()


# In[23]:


obj.enqueue(1)
obj.enqueue(2)


# In[24]:


obj.size


# In[25]:





# In[27]:


##We will implement priority queue by using python list    


# In[488]:





# In[489]:





# In[490]:





# In[491]:





# In[492]:





# In[493]:





# In[494]:





# In[495]:





# In[496]:





# In[497]:





# In[498]:





# In[499]:





# In[500]:





# In[501]:





# In[502]:





# In[503]:





# In[504]:





# In[ ]:




