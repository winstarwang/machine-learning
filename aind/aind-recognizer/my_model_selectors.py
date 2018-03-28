import math
import statistics
import warnings

import numpy as np
from hmmlearn.hmm import GaussianHMM
from sklearn.model_selection import KFold
from asl_utils import combine_sequences


class ModelSelector(object):
    '''
    base class for model selection (strategy design pattern)
    '''

    def __init__(self, all_word_sequences: dict, all_word_Xlengths: dict, this_word: str,
                 n_constant=3,
                 min_n_components=2, max_n_components=10,
                 random_state=14, verbose=False):
        self.words = all_word_sequences
        self.hwords = all_word_Xlengths
        self.sequences = all_word_sequences[this_word]
        self.X, self.lengths = all_word_Xlengths[this_word]
        self.this_word = this_word
        self.n_constant = n_constant
        self.min_n_components = min_n_components
        self.max_n_components = max_n_components
        self.random_state = random_state
        self.verbose = verbose

    def select(self):
        raise NotImplementedError

    def base_model(self, num_states):
        # with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        # warnings.filterwarnings("ignore", category=RuntimeWarning)
        try:
            hmm_model = GaussianHMM(n_components=num_states, covariance_type="diag", n_iter=1000,
                                    random_state=self.random_state, verbose=False).fit(self.X, self.lengths)
            # if self.verbose:
            #     print("model created for {} with {} states".format(self.this_word, num_states))
            return hmm_model
        except:
            if self.verbose:
                print("failure on {} with {} states".format(self.this_word, num_states))
            return None


class SelectorConstant(ModelSelector):
    """ select the model with value self.n_constant

    """

    def select(self):
        """ select based on n_constant value

        :return: GaussianHMM object
        """
        best_num_components = self.n_constant
        return self.base_model(best_num_components)


class SelectorBIC(ModelSelector):
    """ select the model with the lowest Bayesian Information Criterion(BIC) score

    http://www2.imm.dtu.dk/courses/02433/doc/ch6_slides.pdf
    Bayesian information criteria: BIC = -2 * logL + p * logN
    """

    def select(self):
        """ select the best model for self.this_word based on
        BIC score for n between self.min_n_components and self.max_n_components

        :return: GaussianHMM object
        """
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection based on BIC scores
        logLs = dict()
        for num_states in range(self.min_n_components,self.max_n_components+1):
            model = self.base_model(num_states)
            try:
                score = (-2)*model.score(self.X,self.lengths) + 4*math.log(len(self.X))
                if self.verbose:
                    print("word:{},num_state:{},score:{}".format(self.this_word,num_states,score))
            except:
                if self.verbose:
                    print("failure on {} with {} states".format(self.this_word, num_states))
                continue

            logLs[num_states] = score

        if len(logLs):
            best_num_states = min(logLs, key=logLs.get)
        else:
            best_num_states = self.n_constant

        return self.base_model(best_num_states)


class SelectorDIC(ModelSelector):
    ''' select best model based on Discriminative Information Criterion

    Biem, Alain. "A model selection criterion for classification: Application to hmm topology optimization."
    Document Analysis and Recognition, 2003. Proceedings. Seventh International Conference on. IEEE, 2003.
    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.58.6208&rep=rep1&type=pdf
    https://pdfs.semanticscholar.org/ed3d/7c4a5f607201f3848d4c02dd9ba17c791fc2.pdf
    DIC = log(P(X(i)) - 1/(M-1)SUM(log(P(X(all but i))
    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection based on DIC scores
        logLs = dict()
        models = dict()

        for num_states in range(self.min_n_components,self.max_n_components+1):
            model = self.base_model(num_states)
            models[num_states] = model

        for num_states in range(self.min_n_components,self.max_n_components+1):
            try:
                score1 = models[num_states].score(self.X,self.lengths)
            except:
                continue

            score_anti = []
            for k,v in models.items():
                if k != num_states:
                    try:
                        score_i = v.score(self.X,self.lengths)
                    except:
                        continue
                    else:
                        score_anti.append(score_i)
                        
            if len(score_anti):
                score2 = sum(score_anti)/len(score_anti)
            else:
                score2 = 0

            logLs[num_states] = score1 - score2
            if self.verbose:
                print("num_state:{},score:{}=({})-({})".format(num_states,score1-score2,score1,score2))

        if len(logLs):
            best_num_states = max(logLs, key=logLs.get)
        else:
            best_num_states = self.n_constant

        return self.base_model(best_num_states)


class SelectorCV(ModelSelector):
    ''' select best model based on average log Likelihood of cross-validation folds

    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection using CV
        logLs = dict()
        split_method = KFold(5)
        for num_states in range(self.min_n_components,self.max_n_components+1):

            if len(self.sequences) < 5:
                model = self.base_model(num_states)
                try:
                    logLs[num_states] = model.score(self.X,self.lengths)
                except:
                    pass
                
                continue

            val_scores = 0
            for cv_train_idx, cv_test_idx in split_method.split(self.sequences):    
                try:
                    model = GaussianHMM(n_components=num_states, covariance_type="diag", n_iter=1000,
                                        random_state=self.random_state, verbose=False).fit(combine_sequences(cv_train_idx,self.sequences))
                    val_scores += model.score(combine_sequences(cv_test_idx,self.sequences))
                except:
                    if self.verbose:
                        print("failure on {} with {} states".format(self.this_word, num_states))
                    continue
            
            logLs[num_states] = val_scores/split_method.get_n_splits()
        
        best_num_states = max(logLs, key=logLs.get)

        return self.base_model(best_num_states)

