class People(object):
    def set_age(self, new_age):
        '''
        年龄0~100岁，如果大于100或小于0时就归零
        :return:
        '''
        if new_age > 0 and new_age <= 100:
            self.age = new_age
        else:
            self.age = 0

    def get_age(self):
        return self.age

amy = People()
amy.set_age(20)
print(amy.get_age())
