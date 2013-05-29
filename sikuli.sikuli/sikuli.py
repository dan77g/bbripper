#click("1369700144268.png")

from sikuli.Sikuli import *
 
class Foxenbeef(object):

    def startenAppen(self):
        App.open("/usr/bin/firefox")
        

beefnhelda = Foxenbeef()
beefnhelda.startenAppen()