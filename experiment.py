# 1. load dataset
# 2. load LLaMA
# 3. send each statement through LLaMA up to layer N, sampling output
# 4. do PCA
# 5. plot on top D principal components (w/ classification labels from dataset) and show R^2

import pandas as pd
import numpy as np
import sys
from tqdm import tqdm
from pathlib import Path

from llama import LLaMa
from pca import PCA2d

name = sys.argv[1]

llama = LLaMa.build("weights/LLaMA/7B","weights/LLaMA/7B/tokenizer.model")

df = pd.read_csv(f"datasets/{name}.csv")

samples = []
for statement in tqdm(df['statement']):
    residual = llama.call_upto(12, statement).numpy()
    samples.append(residual)

samples = np.array(samples) # (250,1,4096)
samples = np.squeeze(samples, axis=1) # (250, 4096)

basis, residuals = PCA2d(samples)
projection = samples @ basis

with open(f"{name}.csv","w") as f:
    for i,sample in enumerate(projection):
        pc1 = sample[0]
        pc2 = sample[1]
        label = df['label'][i]
        f.write(f"{pc1}\t{pc2}\t{label}\n")

with open(f"{name}-residuals.csv","w") as f:
    for i,r_squared in enumerate(residuals):
        f.write(f"{i}\t{r_squared}\n")
