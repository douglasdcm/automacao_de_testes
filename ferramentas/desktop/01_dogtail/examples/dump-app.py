import dogtail.tc
from dogtail.procedural import run, click
from dogtail import tree


# Load our persistent Dogtail objects
TestString = dogtail.tc.TCString()

# Start app.
run("gnome-calculator")


app = tree.root.application("gnome-calculator")
app.dump()
click("Close")
