#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import torch

def main():
    print "we are in %s"%__name__
    #y=torch.Tensor(4,2,3)
    #print y
    print torch.cuda.is_available()
    x=torch.rand(4,3)
    y=torch.rand(4,3)
    print x,y
    if(torch.cuda.is_available()):
        print "cuda is true!"
        x=x.cuda()
        y=y.cuda()
    print(x+y)
if __name__ == '__main__':
    main()