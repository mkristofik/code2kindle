# code2kindle
**Michael Kristofik** ([kristo605@gmail.com](mailto:kristo605@gmail.com))

code2kindle is a utility for generating a Kindle format e-book from a set of source code files.  It generates html files from your code that a conversion tool (such as [Calibre](http://calibre-ebook.com/)) can use to create an e-book.  Transfer the e-book to your Kindle, and you can read and annotate code anywhere you go.

## Reading code on a Kindle?  Really?

Yes, really.  Here are a few reasons why:

- I already have a Kindle and don't want to buy a tablet.
- I already carry my work laptop and work phone on the train. For legal reasons, I'm avoiding any use of company resources when developing open-source code.
- The Kindle is an excellent platform for reading.
- The annotate feature lets me make notes and corrections to be incorporated later.

## How to use

1. `python code2kindle.py <source-dir>`
2. Click-and-drag the produced `code.html` file into Calibre.
3. Select the 'code' book and press Convert Books.
4. Edit e-book metadata as desired.
5. Send the generated e-book to your Kindle.

## Requirements

Python 2.6+  
Calibre  
Kindle

## License

Copyright Michael Kristofik 2013.  
Distributed under the Boost Software License, Version 1.0.  
See accompanying file `LICENSE_1_0.txt` or [online copy](http://www.boost.org/LICENSE_1_0.txt).

