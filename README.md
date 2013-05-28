bbripper
========

Project to scrape/rip certain content from the web

Objective:
- Mirror complete structure of Bluebook archive on ______.com (using scrapy)
- Download each image as JPEG into appropriate folder (using sikuli)
- Convert JPEG list into multi-page PDF for each report (use ImageMagick "convert", eg "convert *.jpg file.pdf")
- Do OCR on multi-page report (use pdfocr - has cuneiform as dep) 
	- use tesseract-ocr , follow pdfocr as example
	- use textcleaner to prime jpeg image http://www.fmwconcepts.com/imagemagick/textcleaner/index.php
	- possibly use some adaptive algorithm as outlined on http://vbridge.co.uk/2012/11/05/how-we-tuned-tesseract-to-perform-as-well-as-a-commercial-ocr-package/
	