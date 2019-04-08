#!/bin/bash

stringZ=abcABC123ABCabc

echo  stringZ= $stringZ
echo len of regex abc\[A-Z\]*.2= `expr "$stringZ" : 'abc[A-Z]*.2'`
echo substring\(stringZ,2\)= ${stringZ:3}
echo  replace acb with xyz= ${stringZ/abc/xyz}
