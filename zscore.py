# -*- coding: utf-8 -*-
"""
Created on Thu May  7 21:43:08 2020

@author: SHUBHAM KAMBOJ
"""

import scipy.stats as st

def Zscore(p):
    return(print("z0-value = ",st.norm.ppf(p)))
  
def chisqscore(p, dof):
    return(print("\n z0-value   = ",st.chi.ppf(p, dof)))
  

def tscore(p, dof):
      return(print("\n z0-value  = ",st.t.ppf(p,dof)))


def fscore(p, dof1, dof2):
      return(print("\n z0-value  = ",st.f.ppf(p,dof1 , dof2)))

Zscore(0.9772498680518208)
chisqscore(0.9560630663765926,2)
tscore(0.9933281724887152,10)
fscore(0.6666666666666666, 2, 1)