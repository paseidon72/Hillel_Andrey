class Segment1(object):

    def __init__(self, start=0, finish=0):
        self.start = start
        self.finish = finish

    def __str__(self):
        return f"{self.start}, {self.finish}"

    @staticmethod
    def is_crossed(seg1, seg2):
        if seg1.finish < seg2.start or seg2.finish < seg1.start:
            return False
        return True


s1 = Segment1(2, 5)
s2 = Segment1(3, 7)


print(Segment1.is_crossed(s1, s2))
