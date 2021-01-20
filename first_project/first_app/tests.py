from django.test import TestCase

# Create your tests here.

class topics():
    def __init__(self,topics):
        print("inside init")
        self.topics=topics


    def __str__(self):
        print('Inside __str__')
        return "My topic is " + self.topics

my_top = topics("News")
print(my_top)
