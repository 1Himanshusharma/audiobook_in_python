#make sure you have install pypdf2 and pyttsx in your system
#you can install those libraries by run these commands in terminal
#pip install pyPDF2
#pip install pyttsx3

# now we can write down over code

import PyPDF2
import pyttsx3

# path of your file
pdf_path = r'file_path in your system'

#opening the file
pdf_file = open(pdf_path, 'rb')

#reading the pdf file
pdfReader = PyPDF2.PdfReader(pdf_file)

#initialising the speaker engine
speaker = pyttsx3.init()

#accessing each pages in pdf 
for page_num in range(len(pdfReader.pages)):
  
  #extracting the text from the file
  text = pdfReader.pages[page_num].extract_text()
  
  #speaking out the text
  speaker.say(text)

#saving the audio file 
speaker.save_to_file(text,'c:\\audio.mp3')

#stop speaking
speaker.runAndWait()

#closing the file
pdf_file.close()
