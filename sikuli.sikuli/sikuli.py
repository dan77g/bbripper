from sikuli.Sikuli import *
 
class Firefox(object):

    def startApp(self):
        ff = App.open("/usr/bin/firefox http://www.fold3.com/image/7072575/")
        wait(8)
        click("1369871703300.png")
        click("1369871760039.png")

        wait(2)
        ff.focus("Select location for download by www.fold3.com")

        click("1369909550312.png")

        click("1369909288226.png")
        
        

app = Firefox()
app.startApp()