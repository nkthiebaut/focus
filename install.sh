#!/bin/bash
for line in $(cat requirements.txt)
do
   pip3 install ${line}
done

python3 setup.py install

python3 -m spacy download en
python3 -m nltk.downloader punkt
