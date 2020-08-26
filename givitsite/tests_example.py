from django.test import TestCase

# That's how it should look like.


class exampleTest(TestCase):
    def setup(self):
        test1 = 1
        test2 = 2

    def laws_of_math_still_aplly(self):
        "If I remember correctly this should work:"
        self.assertEqual(self.test1 + self.test1,self.test2)