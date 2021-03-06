#!/usr/local/bin/python
# Fig. 6.10: fig06_10.py
# Demonstrates use of cgi.FieldStorage with an XHTML form.

import cgi

def printHeader( title ):
   print """Content-type: text/html

<?xml version = "1.0" encoding = "UTF-8"?>    
<!DOCTYPE html PUBLIC
   "-//W3C//DTD XHTML 1.0 Strict//EN"
   "DTD/xhtml1-strict.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml">
<head><title>%s</title></head>

<body>""" % title

printHeader( "Using cgi.FieldStorage with forms" )
print """<p>Enter one of your favorite words here:<br /></p>
   <form method = "post" action = "fig06_10.py">
      <p>
      <input type = "text" name = "word" />
      <input type = "submit" value = "Submit word" />
      </p>
   </form>"""

form = cgi.FieldStorage()

if form.has_key( "word" ):
   print """<p>Your word is:  
      <span style = "font-weight: bold">%s</span></p>""" \
      % cgi.escape( form[ "word" ].value )

print "</body></html>"

########################################################################## 
# (C) Copyright 2002 by Deitel & Associates, Inc. and Prentice Hall.     #
# All Rights Reserved.                                                   #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
