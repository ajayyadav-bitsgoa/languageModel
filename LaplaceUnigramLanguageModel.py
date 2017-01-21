import math, collections
class LaplaceUnigramLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    self.unigramCounts = collections.defaultdict(lambda: 0)
    self.total = 0
    # TODO your code here
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    for sentence in corpus.corpus:
      for datum in sentence.data:
        token = datum.word
        self.unigramCounts[token] = self.unigramCounts[token] + 1
        self.total += 1
    # TODO your code here
    #pass

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # TODO your code here

    score = 0.0 
    #when model is not learning, just predicting the most relevant output

    for token in sentence:
      count = self.unigramCounts[token]
      score += math.log(count+1) - math.log(self.total + len(self.unigramCounts))
    


    # when you want the model to parallely learn also through test examples.
    # but this has a flwa. figure out. ;)

"""
    for token in sentence:
      count = self.unigramCounts[token]
      if count > 0:
       score += math.log(count+1) - math.log(self.total + len(self.unigramCounts))
      
      else:  
        for word in self.unigramCounts:
            unigramCounts[word] += 1
            self.total += 1

        self.unigramCounts[token] += 1
        self.total += 1

        score += math.log(count+1) - math.log(self.total + len(self.unigramCounts))
"""
# you want the algo to learn, but then it will also become part of training set. So why increase frequency of every word.
#just increase its count and total word count.

    return score
