This is software for reproducing the experiment performed in [_The
Geometry of Truth: Emergent Linear Structure in Large Language Model
Representations of True/False
Datasets_](https://arxiv.org/abs/2310.06824) by Samuel Marks and Max
Tegmark. For my purposes, M2 Macbook and no GPU, this reduces the time
to run an experiment from a long night's rest to sub five minutes.

Large Language Models process input with an ordered sequence of
layers. Let $l_i(x)$ denote the result of calling the $i$th layer on
some input $x$; The value returned by a model with three layers is
denoted $M(x) = l_3(l_2(l_1(x)))$.

This software analyzes the output of $l_{12}$ (of $32$) of
[Meta's](https://arxiv.org/pdf/2302.13971.pdf) seven billion parameter
LLM (LLaMA-7b). It takes a set of statements and sends them through
the first twelve layers of LLaMA-7b sampling the output. It then
performs principal component analysis to find a two-dimensional basis
for each sample and creates a plot of each statement projected onto
that basis.

Here is an example plot produced with this software, and with a legend
and a little tweaking in Figma.

![](/maths-demo.svg)

If you are curious about what statements created this plot you might enjoy
[this essay](https://percisely.xyz/the-geometry-of-truth).

## Using this software

1. Create python virtual environment `python3 -m venv topology`.
2. Activate the virtual environment `source topology/bin/activate`.
3. To deactivate, run `deactivate`.
4. LLaMA weights are expected in a directory called `weights/` which
   you will need to create. They should be in files ending in the
   `.pth` format. For example, to use LLaMA-7b, you might clone
   [https://huggingface.co/nyanko7/LLaMA-7B/tree/main] into
   `weights/LLaMA/7B`.

The `datasets/` directory is in the same format as the one used in the
paper's code which can be found
[here](https://github.com/saprmarks/geometry-of-truth/tree/91b223224699754efe83bbd3cae04d434dda0760/datasets). If
you'd like to reproduce some of the author's experiments copying the
contents of that folder into `datasets/` will let you do so.

To run an experiment, run `./run.sh experiment <datasetname>`. For
example, to run an experiment using the maths dataset: `./run.sh
experiment maths`. This will create two plots one containing the
projection of each datapoint onto its top two principal components,
and one containing a plot of the fraction of the variance of the
original data as a function of the number of principal components used
in a projection. See Appendix I of the aforementioned essay for more
explanation about the later plot.

`llama.py` contains the LLaMa implementation in tinygrad/examples,
with a `call_upto` method added which returns the state of the
residual stream after N layers and stops. I believe this is where the
majority of the speedup comes from. The author's code appears to
evaluate all of the layers of the LLM, whereas this bails out after
collecting the sample it needs.
