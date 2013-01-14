#import ElementTree
from xml.etree import ElementTree 
#set input file
import Tkinter,tkFileDialog
root = Tkinter.Tk()
file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
tree = ElementTree.parse(file) 
# load all of the name columns and check if they start with VFX_ (to search another column - replace //name with the name of the column)
for searchresult in tree.findall("//length"): 
	# list found results
	print "Found this: ", searchresult.text
	searchresult.text="1"
	print "Changed to this: ", searchresult.text
		

#write results back to new file
myFormats = [
    ('SCRATCH XML','*.xml')]

root = Tkinter.Tk()
fileName = tkFileDialog.asksaveasfilename(parent=root,filetypes=myFormats ,title="Save the file as...")
if len(fileName ) > 0:
	tree.write(fileName)