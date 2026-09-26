# Email Extractor using Python

A simple Python automation project that reads a text file, identifies email addresses from its content, and saves the extracted email addresses into a separate output file.

This project was developed as part of my **CodeAlpha Python Programming Internship — Task 3: Task Automation with Python Scripts**.

---

## About the Project

While working with text files, manually searching for email addresses can become repetitive, especially when the file contains a large amount of text.

This project automates that small task.

The program:

1. Reads contact information from a text file.
2. Searches the content for email addresses.
3. Extracts all matching email addresses.
4. Removes duplicate addresses.
5. Saves the final list into a separate text file.
6. Displays the extracted addresses and their total count in the terminal.

The project is intentionally kept simple so that the core Python concepts behind the automation are easy to understand.

---

## Objective

The main objective of this project is to practice using Python for a practical file-processing task.

Through this project, I worked with:

- File handling
- Regular expressions
- Lists
- Loops
- String processing
- Basic automation
- Reading and writing text files

---

## Technologies Used

- **Python 3**
- **Regular Expressions (`re` module)**
- **Text File Handling**

No external libraries are required.

---

## Project Structure

```text
CodeAlpha_EmailExtractor/
│
├── email_extractor.py
├── contact_data.txt
├── extracted_emails.txt
└── README.md
