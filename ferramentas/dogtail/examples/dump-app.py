import dogtail.tc
from dogtail.procedural import *


# Load our persistent Dogtail objects
TestString = dogtail.tc.TCString()

# Start app.
run("gnome-calculator")

from dogtail import tree

app = tree.root.application("gnome-calculator")
app.dump()
click("Close")
