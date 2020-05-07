# -*- coding: utf-8 -*-
"""
Created on Thu May  7 21:03:23 2020

@author: SHUBHAM KAMBOJ
"""

import scipy.stats as st

def Z_prob(z0):
    return(print('p-value of z normal distribution = ',st.norm.cdf(z0)))


def chi_prob(z0, dof):
      return(print('\np-value of chisquare  = ',st.chi.cdf(z0, dof)))

def t_prob(z0, dof):
        return(print('\np-value of t distribution = ',st.t.cdf(z0,dof)))


def f_prob(q,dof1, dof2):
      return(print('\np-value of f distribution = ',st.f.cdf(q,dof1 , dof2)))


Z_prob(2)
chi_prob(2.5,2)
t_prob(3, 10)
f_prob(4,2,1)