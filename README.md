# OOXML-MalClassifier
This project is a fork from [OOXML-MalClassifier](https://github.com/sharpduckk/OOXML-MalClassifier).

Only difference is...
- Added ZIP structure analysis
- Added GUI

## Installation
Run `setup.py`. Package `ooxml_malclassifier` must be initialized.

And run `gui.py` to begin.

## How to analysis

1. Set `folder path` where OOXML files are.
2. Click `scan` Button. It will produce ZIP analysis logs in plaintext widget.
3. When all analysis is done, It will show items which represent each file analysis results.
4. Click one of listItems to read JSON result.
5. All results in `output.json` file.

![ooxml_malclassifier_gui_result](https://user-images.githubusercontent.com/86000275/221517489-543aa22c-8e1a-4677-aa07-3c8c9c8c2a62.png)

## Framework Overview
![model](https://user-images.githubusercontent.com/25279893/76674222-3b51e280-65f0-11ea-92f8-2b4ec00bf779.jpg)
