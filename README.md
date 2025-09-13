[![PyPI Version](https://img.shields.io/pypi/v/searchallpdf)](https://pypi.org/project/searchallpdf/)
[![License](https://img.shields.io/github/license/casiez/searchallpdf)](LICENSE)

# searchallpdf

searchall pdf uses PyMuPDF to extract text from pdf files. If no text is found on a page, it uses OCR (pytesseract) to extract text from images.

Command line to search in pdf files
## Install
```pip install searchallpdf --upgrade```

## Features

Run ```searchallpdf -h``` to show all the options available.

### Search in all pdf files in current and sub folders

```searchallpdf termTofind1 termTofind2```

### Search in one pdf file

```searchallpdf -f file.pdf termTofind1 termTofind2```


