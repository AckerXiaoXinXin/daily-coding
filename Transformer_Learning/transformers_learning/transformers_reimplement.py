import torch
import torch.nn as nn
import torch.functional as F
import math


class PositionalEncoding(nn.Module):
    def __init__(self, d_model, dropout=0.1, max_len=5000) -> None:
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float() * (-math.log(10000.0)/d_model))
        pe[:,0::2] = torch.sin(position * div_term)
        pe[:,1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0).transpose(0,1)
        self.register_buffer('pe', pe)
    
    def forward(self, x):
        x = x + self.pe[:x.size(0),:]
        return self.dropout(x)
    

class TransformerModel(nn.Module):
    def __init__(self, vocab_size, d_model, nhead, num_encoder_layers, 
                 num_decoder_layers, dim_feedford, dropout) -> None:
        super(TransformerModel, self).__init__()
        self.model_type = 'Transformer'
        self.src_embedding = nn.Embedding(vocab_size, d_model)
        self.tgt_embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoder = PositionalEncoding(d_model, dropout)
        self.pos_decoder = PositionalEncoding(d_model, dropout)
        self.transformer = nn.Transformer(d_model, nhead, num_encoder_layers, 
                 num_decoder_layers, dim_feedford, dropout)
        self.fc_out = nn.Linear(d_model, vocab_size)
        self.d_model = d_model

    def forward(self, src, tgt, src_mask=None, tgt_mask=None, memory_mask=None):
        src = self.src_embedding(src) * math.sqrt(self.d_model)
        tgt = self.tgt_embedding(tgt) * math.sqrt(self.d_model)
        src = self.pos_encoder(src)
        tgt = self.pos_decoder(tgt)
        memory = self.transformer(src, tgt, src_mask, tgt_mask, memory_mask) 
        output = self.fc_out(memory)
        return output
    



    