this repository contains bunch of experiences on [MedNli dataset](https://paperswithcode.com/dataset/mednli).
remember to upload the dataset files (in parquet format) before running the notebooks.

# experiments
Here it is the ways that i experimented for textual inference on Mednli dataset, my best model had 77% accuracy which has under 10% difference with SOTA accuracy.
## Sci5
[SciFive](https://github.com/justinphan3110/SciFive) is the state of the art for medical language inference, this language model achieved 86% accuracy on MedNli dataset.
you can use [this notebook](https://github.com/Mehrdadghassabi/Mednli_experiments/blob/main/Sci5/Untitled63.ipynb) to evaluate its performance

## Simple feed forward
for textual inference the most simple idea that comes to mind is to extract premise and hypothesis word embedding concatenating them and within a simple feed forward layer do the classification task.
it can achieve about 68% accuracy on MedNli dataset.
read [this article](https://aclanthology.org/D15-1075/) and
see [this notebook](https://github.com/Mehrdadghassabi/Mednli_experiments/blob/main/Simple_feed_forward/Notebooks/Untitled59.ipynb) for further informations.

## Recurrent neural networks
another idea is to give premise and hypothesis within a start token to a recurrent neural network module (LSTM for example) and then use the last hidden layer of the module
for classification.
see [this notebook](https://github.com/Mehrdadghassabi/Mednli_experiments/blob/main/Recurrent_NN/Notebooks/Untitled64.ipynb) or
[this notebook](https://github.com/Mehrdadghassabi/Mednli_experiments/blob/main/Recurrent_NN/Notebooks/Untitled65.ipynb)
for further informations.

## Recurrent neural networks with Attention
inspired by [this article](https://arxiv.org/pdf/1509.06664) we used an attention module to further contextualize the embeddings it achieved about 69% accuracy on MedNli dataset.
see [this notebook](https://github.com/Mehrdadghassabi/Mednli_experiments/blob/main/Recurrent_NN_with_Attention/Notebooks/Untitled66.ipynb)
or [this notebook](https://github.com/Mehrdadghassabi/Mednli_experiments/blob/main/Recurrent_NN_with_Attention/Notebooks/Untitled67.ipynb)
for further informations.

## Interaction space (incomplete)
inspired by [this article](https://arxiv.org/abs/1802.03198) Ive implemented a neural network to do the inference based on interaction space
see [this notebook](https://github.com/Mehrdadghassabi/Mednli_experiments/blob/main/Interaction_space/Untitled71.ipynb) for further informations.

## Transformers
using the famous [attention is all you need paper](https://arxiv.org/abs/1706.03762) encoder we enhanced contexualizing of premise and hypothesis and then
taking hadamard product of embeddings we do a classification task, it achieved 75% accuracy on MedNli dataset.
[this notebook](https://github.com/Mehrdadghassabi/Mednli_experiments/blob/main/Transformers/Notebooks/Untitled68.ipynb) have done this using Early stoping,
[this one](https://github.com/Mehrdadghassabi/Mednli_experiments/blob/main/Transformers/Notebooks/Untitled70.ipynb) have done it without Early stoping
and [this one](https://github.com/Mehrdadghassabi/Mednli_experiments/blob/main/Transformers/Notebooks/Untitled62.ipynb) have done it with freezing word embedding layer.

## Augmented transformers
using previous way we did some Augmentation on datas using text attack library see [this notebook](https://github.com/Mehrdadghassabi/Mednli_experiments/blob/main/Augmented_transformers/Untitled76.ipynb) for further informations.

## Selector (incomplete)
having a neural network that do the inference for us we used another neural network to decide whether this network is sure about its decison or not,
then for the examples that the neural network is unsure about it we can use another agent.

## Recurrent neural networks with transformers
the idea is to give the contextualized embedding of the transformers to a Recurrent neural network,
see [this notebook](https://github.com/Mehrdadghassabi/Mednli_experiments/blob/main/RNN_with_transformers/Untitled72.ipynb) for further informations.

## hybrid AI
inspired by [this](https://aclanthology.org/2020.coling-main.459/) and [this](https://www.igi-global.com/chapter/a-lexico-syntactic-semantic-approach-to-recognizing-textual-entailment/247903) articles we enhanced our accuracy to 76%
by combining symbolic and deep AI, 
see [this notebook](https://github.com/Mehrdadghassabi/Mednli_experiments/blob/main/Hybrid_AI/Untitled60.ipynb) for implementing it using the selector network.
and see [this notebook](https://github.com/Mehrdadghassabi/Mednli_experiments/blob/main/Hybrid_AI/Untitled61.ipynb) for implementing it without the selector network.

## Acknowledgement
thanks to [this implemention](https://github.com/ChrisBenka/transformers) of transformers, i used it with slight changes in my code.
