# Keyword Extraction with Character-level Convolutional Neural Tensor Networks
## 1. Introduction
Keywordextractionisacriticaltechniqueinnaturallanguageprocess- ing. For this essential task we present a simple yet efficient architecture involving character-level convolutional neural tensor networks. The proposed architecture learns the relations between a document and each word within the document and treats keyword extraction as a supervised binary classification problem. In contrast to traditional supervised approaches, our model learns the distributional vector representations for both documents and words, which directly embeds semantic information and background knowledge without the need for handcrafted features.
Most importantly, we model semantics down to the character level to capture morphological information about words, which although ignored in related lit- erature effectively mitigates the unknown word problem in supervised learning approaches for keyword extraction. In the experiments, we compare the proposed model with several state-of-the-art supervised and unsupervised approaches for keyword extraction. Experiments conducted on two datasets attest the effectiveness of the proposed deep learning framework in significantly outperforming several baseline methods.

### 1.1. Requirements
- python2.7
- Chainer
- nltk

### 1.2. Datasets

We provide two dataset, SemEval2013 and Inspec, and the original version is from
https://github.com/snkim/AutomaticKeyphraseExtraction

```
|--data/
  |--semeval_wo_stem
  |--inspec_wo_stem
```

The dataset we used is from Hulth2003 and SemEval2010 with removing stopwords and stemming.

### 1.3. Getting Started
#### Download
```
$ git clone https://github.com/cnclabs/CNTN
$ cd ./CNTN
```

#### Install python packages:
```
$ pip install -r requirements.txt
```

## 2. Usage
### 2.1 Preprocess 
Data preporcessing is following by 
https://github.com/Tixierae/EMNLP_2016

### 2.2 Train a new model
```
$ python train.py
```

### 2.3 Get the keywords from a document
```
$ python predict.py
```

#### Parameters
```
$ python train.py -h
usage: Training [-h] [--dlen DLEN] [--wlen WLEN] [--wdim WDIM] [--hdim HDIM]
                [--label LABEL] [--flen FLEN] [--c C] [--b B] [--e E]
                [--model MODEL] [--train TRAIN] [--predict PREDICT]

Arguments

optional arguments:
  -h, --help            show this help message and exit
  --dlen DLEN, -dl DLEN
                        doc len
  --wlen WLEN, -wl WLEN
                        word len
  --wdim WDIM, -wd WDIM
                        word dim
  --hdim HDIM, -hd HDIM
                        hidden dim
  --label LABEL, -l LABEL
                        output label
  --flen FLEN, -fl FLEN
                        filter length
  --c C, -c C           channel size
  --b B, -b B           batch size
  --e E, -e E           epoch
  --model MODEL, -model MODEL
                        path of model
  --train TRAIN, -train TRAIN
                        path of training data
  --predict PREDICT, -predict PREDICT
                        path of predicted data
```


## 3. Citation
```
```
