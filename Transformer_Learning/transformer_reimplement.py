"""
Project Name: LLM_LEARNING
Module Description: Reimplement transfromer with torch..
Author: lixin
Date: 2024-07-10
Version: 1.0.0
Email: 395095201@qq.com, zangaixiaoxinxin@gmail.com

Description:
    None.

Usage:
    None.

Examples:
    If applicable, include a simple usage example.

Todo:
    - Reimplement transfromer with torch.

@file: LLM_LEARNING
@software: Visual Studio Code
"""


import torch
import torch.nn as nn
import math


# define the Positional Encoding class
class PositionalEmbedding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super(PositionalEmbedding, self).__init__()

        # create a positional encoding tensor 
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)

        div_term = torch.exp(torch.arange(0, d_model, dtype=torch.float) *
                              (-math.log(10000.0)/d_model))
        
        # use sin and cos in positional encoding
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0).transpose(0, 1)

        self.register_buffer('pe', pe)

    def forward(self, x):
        x = x + self.pe[:x.size(0), :]
        return x
    

class TransformerModel(nn.Module):
    def __init__(self, ntoken, d_model, nhead, nhid, nlayers, dropout=0.5):
        super(TransformerModel, self).__init__()
        self.model_type = 'Transformer'

        # define word embedding layer
        self.src_mask = None
        self.encoder = nn.Embedding(ntoken, d_model)
        self.pos_encoder = PositionalEmbedding(d_model)

        # define transformer encoder layer
        encoder_layers = nn.TransformerEncoderLayer(d_model, nhead, nhid, dropout)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layers, nlayers)

        # define final full connection layer
        self.d_model = d_model
        self.decoder = nn.Linear(d_model, ntoken)

        # initial weight
        self.init_weights()
    
    def init_weights(self):
        initrange = 0.1
        self.encoder.weight.data.zero_()
        self.decoder.bias.data.zero_()
        self.decoder.weight.data.uniform_(-initrange, initrange)
        
    def generate_square_subsequent_mask(self, sz):
        mask = (torch.triu(torch.ones(sz, sz)) == 1).transpose(0, 1)
        mask = mask.float().masked_fill(mask==0, float('-inf')).masked_fill(mask==0, float(0.0))
        return mask
    
    def forward(self, src, src_mask):
        src = self.encoder(src) * math.sqrt(self.d_model)

        src = self.pos_encoder(src)

        output = self.transformer_encoder(src, src_mask)

        output = self.decoder(output)
        return output
    

# Parameter setting
ntokens = 1000 
emsize = 512
nhid = 2048
nlayers = 6
nhead = 8
dropout = 0.2

# create a model instance
model = TransformerModel(ntokens, emsize, nhead, nhid, nlayers, dropout)

# print model
print(model)









