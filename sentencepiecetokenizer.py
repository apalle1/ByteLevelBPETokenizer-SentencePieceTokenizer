# -*- coding: utf-8 -*-
"""SentencePieceTokenizer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ABqMdqywXmgm_OM3uBtjNQ5vo9QDVQ85

Sentencepiece is pretty cool because it is a language-independent subword tokenizer.

**Sentencepiece repository:** 
https://github.com/google/sentencepiece

**Sentencepiece python implementation:** https://github.com/google/sentencepiece/blob/master/python/sentencepiece_python_module_example.ipynb
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/content/drive')
# %cd /content/drive/My Drive/Tweet Sentiment Extraction Final

!pip install transformers
!pip install sentencepiece

import sentencepiece as spm
sp = spm.SentencePieceProcessor()
sp.load('./input/albert-configs/albert-large-v2/spiece.model')

sp.encode_as_pieces('the quick brown fox jumps over the lazy dog')

sp.encode_as_ids('the quick brown fox jumps over the lazy dog')

pieces = sp.encode_as_pieces('the quick brown fox jumps over the lazy dog')
"".join(pieces).replace("▁", " ").strip()

import sys
sys.path.insert(0, './input/sentencepiece_pb2/')

import sentencepiece_pb2

spt = sentencepiece_pb2.SentencePieceText()
sp = spm.SentencePieceProcessor()
sp.load('./input/albert-configs/albert-large-v2/spiece.model')

spt.ParseFromString(sp.encode_as_serialized_proto('the quick brown fox jumps over the lazy dog'))
print(spt)

class SentencePieceTokenizer:
  def __init__(self, model_path):
    self.sp = spm.SentencePieceProcessor()
    self.sp.load(os.path.join(model_path, 'spiece.model'))
  
  def encode(self, sentence):
    spt = sentencepiece_pb2.SentencePieceText()
    spt.ParseFromString(self.sp.encode_as_serialized_proto(sentence))
    offsets = []
    tokens = []
    for piece in spt.pieces:
      tokens.append(piece.id)
      offsets.append((piece.begin, piece.end))
    return tokens, offsets

import os
class config:
  MODEL_NAME = "albert-large-v2"
spt = SentencePieceTokenizer('./input/albert-configs/albert-large-v2')

spt.encode('the quick brown fox jumps over the lazy dog')

import transformers
spt_trans = transformers.AlbertTokenizer.from_pretrained('./input/albert-configs/albert-large-v2/')
spt_trans.encode('the quick brown fox jumps over the lazy dog')