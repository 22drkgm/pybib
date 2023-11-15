# pybib

A simple Python script for generating BibTeX entries from DOIs in a CSV file.

## Overview

This project provides a Python script (`pybib.py`) that takes a CSV file containing DOIs as input and generates BibTeX entries for references. It uses the Crossref API to retrieve metadata for the given DOIs and creates BibTeX entries in a specified style.

## Features

- **Input:** Accepts a CSV file containing DOIs.
- **Output:** Generates BibTeX entries in a file named `references.bib`.
- **BibTeX Entry Format:** Uses the last name of the first author and the publication year.

## Usage

1. Clone the repository:

   git clone https://github.com/your-username/pybib.git
   cd pybib


##Example 
       python pybib.py --csv your_file.csv

##Configuration
You can customize the output file name in the save_bibtex_entries function within pybib.py.
Dependencies
requests: Used for making HTTP requests.
