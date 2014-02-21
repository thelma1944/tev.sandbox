import xlwt
import  numpy
from selenium import webdriver
import unittest
import django
import os

def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities={
            "browserName": "firefox",
            "platform": "MAC",
        })
        
def test_example(self):
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    
os.chdir ('/working')

wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')

# indexing is zero based, row then column
sheet.write(0,1,'test_text')

# Initialize a style
style = xlwt.XFStyle()
 
# Create a font to use with the style
font = xlwt.Font() # Create the Font
font.name = 'Times New Roman'
font.bold = True
font.size = 14
 
# Set the style's font to this new one you set up
style.font = font
 
# We add a sheet and set the cell to overwite OK.

sheet2 = wbk.add_sheet('TEV_2', cell_overwrite_ok=True)
# Use the style when writing

sheet2.write(0,0,'some text')
sheet2.write(0, 0, 'some bold Times text', style)

#  Now save the workbook
wbk.save('test.xls')
done = '';
