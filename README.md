# python-sandbox
Python sandbox w/ core capabilities 

* pandas, numpy, scipy, 
* matplotlib, 
* BeautifulSoup4
* ml models
   * linear regression w/ scifi
   * natural language processing w/ nlptk
   * n-gram analysis w/ nlptk
   * sentiment analysis w/ nlptk and scikit-learn
   
python notes for [data structures](https://github.com/tansudasli/python-sandbox/wiki/Python-Data-Structures)

# How To Start

create env
```
conda create -n core python=3

conda activate core 

conda install -n core ipykernel
```

1. core : python3 core data structures
2. data : all about data manipulation w/ **pandas** 
   - [x] on local
   - [x] on Dataproc GCP
3. statistics : about statistical ops. w/ **numpy**, **scipy**, 
4. visualization : graphs w/ **matplotlib**, **seaborn**
4. ml : machine learning models such as linear regression, nlp etc..
5. scrapping : about html parsers
6. code-review : about code interviews while hiring data scientists

#### run python from bash-shell

 `echo ls -l | bash`

 `echo "Hello Holly." | python3 -c "import sys; [print(line) for line in sys.stdin]"`

 `echo 3.30 | python3 -c "print('my grade is {}'.format(input()))"`

 