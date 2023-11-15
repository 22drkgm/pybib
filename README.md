# pybib

pybib is a simple Python script designed to generate .bib files from DOIs for references in LaTeX documents. This project addresses the need for a streamlined solution to avoid bulky .bib files, especially when working with large LaTeX documents.

## Motivation

Working with LaTeX documents often involves managing bibliographic references, and existing tools like Mendeley and Zotero, while powerful, may generate bulky .bib files. In my experience, Zotero's default .bib file sometimes doesn't meet my referencing needs, leading to manual modifications. pybib simplifies this process by directly creating .bib files from DOIs, providing a more efficient and customizable solution.

## Usage

1. Install the required dependencies:
  
       pip install -r requirements.txt
 or 

2. Run the script with a DOI to generate a .bib file:
bash

        python pybib.py <DOI>

    
    Example:

        python pybib.py 10.1234/example_doi


   ## Compatibility

pybib is compatible with Python 3.6 and above.

## Requirements

- Python 3.6+



## Feedback and Contributions

Your feedback is valuable! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request. Contributions are highly welcomed.





## License

This project is licensed under the [MIT License](LICENSE).
