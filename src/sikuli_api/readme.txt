*** SikuliX-API-1.0Linux32BetaNNN ***
*** SikuliX-API-1.0Linux64BetaNNN ***
-------------------------------------

Be aware: 
- still work in progress - might contain bugs
- not everything is tested
- not everything is implemented / documented

*** Installation
- unzip to any location you like
- the preferred folder name is SikuliX (but need not be)

*** This package is intended for usage from command line 

*** Using the contained command script
- you can run the command scripts from any working folder using its absolute or relative path
- use sikli-script (interactive or run scripts) this way:
./sikuli-script (supported options: -h (help), -i (interactive), -r (run a script))

*** Java-Version:
- the stuff is compiled with OpenJDK7 latest version on Ubuntu 12.10
- it should run on Oracle's Java 7 and Java 6
- it is run with the current default Java version on your machine
- having more than one Java version on your machine, use option 
  -j 6 to run with your Java 1.6
  -j 7 to run with your Java 1.7
with the above mentioned command scripts
ISSUE: you have to modify the command file to point to the correct Java folders

*** Using sikuli-script.jar in Java programming with IDE's like Netbeans, Eclipse, ...
    or Java based scripting (like Jython, JRuby, Scala, Groovy, Clojure, ...)

look: https://github.com/RaiMan/SikuliX-API/wiki/Usage-in-Java-programming  
