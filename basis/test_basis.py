#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import torch

import numpy as np
def main():
    print "we are in %s" % __name__
    # y=torch.Tensor(4,2,3)
    # print y
    print torch.cuda.is_available()
    x = torch.rand(4, 3)
    y = torch.rand(4, 3)
    print x, y
    if (torch.cuda.is_available()):
        print "cuda is true!"
        x = x.cuda()
        y = y.cuda()
    print(x + y)
    #x从gpu转cpu
    x=x.cpu()
    #tensor转numpy
    z=x.numpy()
    print z
    print type(z)
    #numpy转tensor
    k = torch.from_numpy(z)
    print type(k),k


if __name__ == '__main__':
    main()
