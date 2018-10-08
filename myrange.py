class myrange(object):

    def __init__(self, start, stop=0, step=1):
        self.step = step

        if self.step > 0:
            if stop == 0:
                self.start = 0 - step
                self.stop = start - 1
            else:
                self.start = start - step
                self.stop = stop - 1
            self.check = lambda x,y: x < y
        elif self.step < 0:
            self.start = start - step
            self.stop = stop + 1
            self.check = lambda x,y: x > y
        else:
            raise ValueError("step must not be 0")

    def __iter__(self):
        return  self

    def next(self):

        if self.check(self.start, self.stop):
            self.start += self.step
        else:
            raise StopIteration
        return self.start


for i in myrange(5):
    print i,
print '----'
for i in myrange(1,6,2):
    print i,
print '---'
for i in myrange(5,1,-1):
    print i
for i in myrange(-3):
    print i