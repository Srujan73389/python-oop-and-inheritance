class Father:
    def sleep(self):
        print("sleeps from 10:00 PM to 5:00 AM")
    def eaT(self):
        print("EATING")
class Son(Father):
    def sleep(self):
        pass
        print("sleeps from 2:00 AM to 10:00 AM")
        # Father.sleep(self)
        super().sleep()
s=Son()
s.sleep()