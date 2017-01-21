import math, collections
class LaplaceBigramLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.unigramCounts = collections.defaultdict(lambda: 0)
    self.bigramCounts = collections.defaultdict(lambda : collections.defaultdict(lambda : 0))
    self.train(corpus)
    self.total = 0

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    word = ''
    for sentence in corpus.corpus:
      for datum in sentence.data:
        token = datum.word
        self.unigramCounts[token] = self.unigramCounts[token] + 1
        self.bigramCounts[word][token] = self.bigramCounts[word][token] + 1
        self.total += 1
        word = token

    self.bigramCounts[word][''] = self.bigramCounts[word][''] + 1


  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # TODO your code here
    #when model is not learning, just predicting the most relevant output

    word = sentence[0]
    for token in sentence[1:]:
      biCount = self.bigramCounts[word][token]
      score += math.log(biCount + 1)
      score -= math.log(self.unigramCounts[word] + len(self.unigramCounts))


    """
        if unigramCounts[token] == 0:
            self.unigramCounts[token] += 1
            self.total += 1

        for token in self.unigramCounts:
            bigramCounts[word][token] += 1

        unigramCounts[word] += self.total

    
        score += math.log(biCount + 1)
        score -= math.log(self.unigramCounts[word] + len(self.unigramCounts))  #smoothed
    """
# unnecessary complicated it. lol.

    return score

