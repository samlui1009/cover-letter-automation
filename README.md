# Cover Letter Automation Tool 
<p>The purpose of this miniature project is to create a lightweight tool that automates the process of writing cover letters for job applications. The current output generates Docx files.   

## Usage
To run this script:
1. Open the command-line window, and type the following\
`python cl-converter.py`
2. Install all required dependencies, which can be found in the requirements.txt file. 
3. Set up your .env file at the root directory, creating 2 environment variables. The first should be for your target output folder path (Named <b>OUTPUT_FOLDER_PATH</b>), and your initials (Named <b>WRITER_INITIALS</b>).
4. Create your cover letter templates, and save them as .docx. You can change out the variable names as you'd like in the source code, so long as it matches the name of your actual Word Documents. In my case, I label my templates accordingly in the following way: SWE_CoverLetterTemplate.docx. 
5. When prompted by the interface, enter all pertinent information regarding the job that you wish to write the cover letter for.
6. Upon completion, a new Word Docx file that is now populated with all prior inputs should be accessible in your set output folder path.

## Library Dependencies
<p>For this project, I made use of some well-known Python libraries/modules.</li>
<ol>
<li><b>DocxTemplate</b>:  A library with an easy functionality that generates Microsoft Word (.docx) documents from existing templates.</li>
<li><b>dotenv</b>:  After creating a .env file within your repository, which is used to hide any sensitive data (I.e., API keys, database URLs, secrets), the module is called, and any variables can be loaded from the .env file in the source code. In this case, I utilized it to load directory paths and customize user initials.</li>
</ol>

## References 
<ol>
    <li>https://medium.com/@alice.yang_10652/convert-word-doc-or-docx-to-pdf-with-python-a-comprehensive-guide-6c8e8b5a079a</li>
    <li>https://www.youtube.com/watch?v=bSEKyt_O5Ic</li>
</ol>
