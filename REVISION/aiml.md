# AIML Mock Interview - Master Revision (QnA)

> How to use: Read the **Q**, answer it out loud in your head first, then check the **A**. The "Follow-up / Key points" bullets are what the interviewer will push on next.

**Covers:** Core ML - Algorithms - Model Evaluation - Deep Learning - NLP & Transformers - Generative AI / LLMs

---

## SECTION 1 - CORE MACHINE LEARNING

### Q1. What is the difference between supervised, unsupervised, and reinforcement learning?
**A:** Supervised learning uses labelled data (input-output pairs) to learn a mapping, e.g. classification and regression. Unsupervised learning finds structure in unlabelled data, e.g. clustering and dimensionality reduction. Reinforcement learning trains an agent to take actions in an environment to maximise a cumulative reward signal, learning by trial and error.

**Follow-up / Key points:**
- Supervised: spam detection, house price prediction.
- Unsupervised: customer segmentation, PCA.
- RL: game playing (AlphaGo), robotics, recommendation.
- Semi-supervised = small labelled + large unlabelled; self-supervised = labels generated from the data itself (basis of LLMs).

### Q2. Explain the bias-variance tradeoff.
**A:** Bias is error from wrong assumptions (model too simple, underfits). Variance is error from sensitivity to training data (model too complex, overfits). Total error = bias squared + variance + irreducible error. As model complexity increases, bias falls but variance rises. The goal is the sweet spot that minimises total error.

**Follow-up / Key points:**
- High bias = underfitting: low train AND test accuracy.
- High variance = overfitting: high train, low test accuracy.
- Fix high bias: more features, more complex model. Fix high variance: more data, regularization, simpler model.

### Q3. What is overfitting and how do you prevent it?
**A:** Overfitting is when a model learns noise and specifics of the training data instead of the underlying pattern, so it performs well on training data but poorly on unseen data. Prevent it with more training data, regularization (L1/L2), dropout, early stopping, cross-validation, reducing model complexity, and data augmentation.

**Follow-up / Key points:**
- Signal of overfitting: large gap between train and validation error.
- Underfitting is the opposite - model too simple to capture the pattern.

### Q4. Explain L1 vs L2 regularization.
**A:** Both add a penalty on weights to the loss to discourage large weights. L1 (Lasso) adds the sum of absolute values of weights; it drives some weights to exactly zero, so it does feature selection. L2 (Ridge) adds the sum of squared weights; it shrinks weights smoothly toward zero but rarely to exactly zero.

**Follow-up / Key points:**
- L1 = sparse models, good when many features are irrelevant.
- L2 = handles correlated features better, more stable.
- Elastic Net = combination of both.

### Q5. What is cross-validation and why use it?
**A:** Cross-validation splits the data into k folds, trains on k-1 folds and validates on the remaining fold, rotating until each fold has been the validation set once. The scores are averaged. It gives a more reliable estimate of generalization than a single train/test split and uses data efficiently.

**Follow-up / Key points:**
- k=5 or k=10 are common.
- Stratified k-fold keeps class proportions in each fold (important for imbalanced data).
- Always fit preprocessing (scaling, encoding) inside the CV loop to avoid data leakage.

### Q6. What is data leakage?
**A:** Data leakage is when information from outside the training set (often from the test set or the future) sneaks into model training, giving unrealistically good validation scores that collapse in production. Classic example: scaling or imputing using statistics computed over the full dataset before splitting.

**Follow-up / Key points:**
- Fit scalers/encoders on train only, then transform val/test.
- Target leakage: a feature that is a proxy for the label and would not be available at prediction time.

### Q7. How do you handle missing data?
**A:** Options depend on the amount and pattern: drop rows/columns if missingness is small or a column is mostly empty; impute with mean/median/mode for numeric/categorical; use model-based imputation (KNN, regression); or add a "missing" indicator flag. For tree models, some implementations handle missing values natively.

**Follow-up / Key points:**
- Median is more robust to outliers than mean.
- Understand the mechanism: MCAR, MAR, MNAR - it affects what is safe to do.

### Q8. What is the curse of dimensionality?
**A:** As the number of features grows, the volume of the feature space grows exponentially, so data becomes sparse. Distances between points become less meaningful, models need exponentially more data to generalize, and overfitting risk rises. It particularly hurts distance-based methods like KNN.

**Follow-up / Key points:**
- Mitigate with dimensionality reduction (PCA), feature selection, regularization.

### Q9. Why and how do you scale features?
**A:** Scaling puts features on a comparable range so that no single feature dominates due to its units. Needed for distance-based and gradient-based algorithms (KNN, SVM, neural nets, PCA, logistic/linear regression). Standardization (z-score: subtract mean, divide by std) and Min-Max normalization (scale to 0-1) are the two common methods.

**Follow-up / Key points:**
- Tree-based models (decision trees, random forest, XGBoost) do NOT need scaling - they split on thresholds.
- Standardization for roughly Gaussian data; Min-Max when you need a bounded range.

### Q10. How do you encode categorical variables?
**A:** One-hot encoding creates a binary column per category (good for nominal, low-cardinality features). Label/ordinal encoding maps categories to integers (good for ordinal features with a natural order). Target/mean encoding replaces a category with the mean of the target for that category (powerful for high-cardinality, but watch for leakage).

**Follow-up / Key points:**
- One-hot on high-cardinality features explodes dimensions.
- Tree models can handle label encoding fine; linear models cannot (they assume order).

---

## SECTION 2 - ML ALGORITHMS

### Q11. Explain linear regression and its assumptions.
**A:** Linear regression models the target as a linear combination of features by fitting weights that minimise the mean squared error (via the normal equation or gradient descent). Assumptions: linear relationship, independence of errors, homoscedasticity (constant variance of errors), normally distributed residuals, and little multicollinearity.

**Follow-up / Key points:**
- Cost function: MSE.
- Multicollinearity inflates coefficient variance - check with VIF.

### Q12. How does logistic regression work? Why not use linear regression for classification?
**A:** Logistic regression applies the sigmoid function to a linear combination of features to output a probability between 0 and 1, then thresholds it for classification. It is trained by minimising log loss (cross-entropy). Linear regression is unbounded (can output values outside 0-1) and its squared-error loss is not suited to classification, so logistic regression is used instead.

**Follow-up / Key points:**
- Sigmoid: 1 / (1 + e^-z).
- Decision boundary is linear in feature space.
- Multiclass: softmax / one-vs-rest.

### Q13. How does a decision tree decide splits?
**A:** It greedily picks the feature and threshold that best separate the data according to an impurity measure. For classification it uses Gini impurity or entropy (information gain); for regression it uses variance reduction (MSE). It recursively splits until a stopping criterion (max depth, min samples) is met.

**Follow-up / Key points:**
- Gini: faster; Entropy: information-theoretic - results usually similar.
- Prone to overfitting - control with max_depth, min_samples_leaf, pruning.
- Pros: interpretable, no scaling needed, handles non-linear. Cons: high variance.

### Q14. What is a random forest and why is it better than a single tree?
**A:** A random forest is an ensemble of decision trees trained on bootstrap samples of the data, with each split considering a random subset of features. Predictions are averaged (regression) or majority-voted (classification). The randomness decorrelates the trees, so averaging reduces variance without much increase in bias - much more robust than a single tree.

**Follow-up / Key points:**
- This is bagging + feature randomness.
- Gives feature importance and out-of-bag error estimates.
- Less prone to overfitting than a single deep tree.

### Q15. Explain bagging vs boosting.
**A:** Bagging (Bootstrap Aggregating) trains models in parallel on bootstrap samples and averages them; it mainly reduces variance (e.g. random forest). Boosting trains models sequentially, where each new model focuses on the errors of the previous ones, and combines them as a weighted sum; it mainly reduces bias (e.g. AdaBoost, Gradient Boosting, XGBoost).

**Follow-up / Key points:**
- Bagging: parallel, independent, reduces variance.
- Boosting: sequential, dependent, reduces bias, can overfit if not regularized.

### Q16. How does gradient boosting / XGBoost work?
**A:** Gradient boosting builds trees sequentially; each new tree is fit to the residuals (negative gradients of the loss) of the current ensemble, and is added with a learning rate. XGBoost is an optimized implementation adding regularization, second-order gradients, parallelization, tree pruning, and handling of missing values, making it fast and accurate - a go-to for tabular data.

**Follow-up / Key points:**
- Key hyperparameters: learning_rate, n_estimators, max_depth, subsample.
- Lower learning rate + more trees usually generalizes better.
- LightGBM and CatBoost are popular alternatives.

### Q17. How does SVM work? What is the kernel trick?
**A:** SVM finds the hyperplane that maximises the margin between classes; the closest points are the support vectors. For non-linearly separable data, the kernel trick maps data into a higher-dimensional space implicitly (via a kernel function like RBF or polynomial) so a linear separator exists there, without computing the transformation explicitly.

**Follow-up / Key points:**
- Margin maximisation = better generalization.
- C controls the soft-margin tradeoff (regularization); gamma controls RBF kernel reach.
- Works well in high dimensions; slow on very large datasets.

### Q18. How does KNN work?
**A:** K-Nearest Neighbours is a lazy, instance-based algorithm. To predict, it finds the k closest training points by a distance metric (usually Euclidean) and returns the majority class (classification) or average value (regression). There is no training phase - all computation happens at prediction time.

**Follow-up / Key points:**
- Must scale features (distance-based).
- Small k = noisy/overfit; large k = oversmoothed.
- Slow at inference on large data; suffers curse of dimensionality.

### Q19. Explain Naive Bayes and why it is "naive".
**A:** Naive Bayes applies Bayes' theorem to compute the probability of each class given the features, predicting the most probable class. It is "naive" because it assumes all features are conditionally independent given the class - rarely true, but it works surprisingly well, especially for text classification, and is fast.

**Follow-up / Key points:**
- Variants: Gaussian (continuous), Multinomial (counts, text), Bernoulli (binary).
- Handles high dimensions well; good baseline for spam/sentiment.

### Q20. How does K-means clustering work?
**A:** K-means partitions data into k clusters: initialize k centroids, assign each point to the nearest centroid, recompute centroids as the mean of assigned points, and repeat until convergence. It minimises within-cluster variance (inertia).

**Follow-up / Key points:**
- Must choose k - use the elbow method or silhouette score.
- Sensitive to initialization (use k-means++) and outliers.
- Assumes spherical, similar-sized clusters; scale features first.

### Q21. K-means vs DBSCAN vs hierarchical clustering?
**A:** K-means needs k upfront and finds spherical clusters. DBSCAN is density-based, finds arbitrarily shaped clusters and labels outliers as noise without needing k, but needs eps and min_samples. Hierarchical clustering builds a tree (dendrogram) of nested clusters and lets you cut it at any level, without committing to k in advance.

**Follow-up / Key points:**
- DBSCAN great for non-spherical clusters and noise; struggles with varying density.
- Hierarchical is expensive (O(n^2)+) on large data.

### Q22. Explain PCA.
**A:** Principal Component Analysis is an unsupervised dimensionality-reduction technique. It finds new orthogonal axes (principal components) along the directions of maximum variance, ordered by how much variance they capture, and projects data onto the top components. This reduces dimensions while keeping most of the information.

**Follow-up / Key points:**
- Components are eigenvectors of the covariance matrix (or via SVD).
- Always standardize first.
- Used for compression, visualization, noise reduction; components are not interpretable.

---

## SECTION 3 - MODEL EVALUATION

### Q23. Explain the confusion matrix and the metrics from it.
**A:** A confusion matrix is a table of True Positives, False Positives, True Negatives, and False Negatives. From it: Accuracy = (TP+TN)/total; Precision = TP/(TP+FP) (of predicted positives, how many are correct); Recall = TP/(TP+FN) (of actual positives, how many were caught); F1 = harmonic mean of precision and recall.

**Follow-up / Key points:**
- Precision matters when false positives are costly (spam filter).
- Recall matters when false negatives are costly (cancer detection, fraud).
- F1 balances both - useful on imbalanced data.

### Q24. When is accuracy a bad metric?
**A:** On imbalanced datasets. If 95% of samples are one class, a model predicting only that class gets 95% accuracy while being useless. In such cases use precision, recall, F1, ROC-AUC, or PR-AUC instead.

**Follow-up / Key points:**
- Fraud detection, disease diagnosis - always imbalanced.
- PR-AUC is more informative than ROC-AUC under heavy imbalance.

### Q25. What is ROC-AUC?
**A:** The ROC curve plots True Positive Rate (recall) against False Positive Rate across all classification thresholds. AUC is the area under it - the probability that the model ranks a random positive higher than a random negative. AUC of 0.5 is random, 1.0 is perfect. It measures ranking quality independent of threshold.

**Follow-up / Key points:**
- Threshold-independent.
- Use PR curve instead when positives are rare.

### Q26. Precision-recall tradeoff - explain.
**A:** Lowering the classification threshold catches more positives (higher recall) but also more false positives (lower precision), and vice versa. You tune the threshold based on the business cost of false positives vs false negatives. The PR curve visualizes this tradeoff.

**Follow-up / Key points:**
- Default threshold 0.5 is rarely optimal - tune it.

### Q27. What regression metrics do you know?
**A:** MAE (mean absolute error) - average absolute difference, robust to outliers, same units as target. MSE (mean squared error) - penalizes large errors more, in squared units. RMSE - square root of MSE, back in original units. R squared - proportion of variance explained (1 is perfect, 0 is baseline mean).

**Follow-up / Key points:**
- RMSE more sensitive to outliers than MAE.
- Adjusted R squared penalizes adding useless features.

### Q28. How do you handle an imbalanced dataset?
**A:** At the data level: oversample the minority (SMOTE), undersample the majority. At the algorithm level: use class weights / cost-sensitive learning. At the evaluation level: use F1, PR-AUC, recall instead of accuracy. Also consider threshold tuning and anomaly-detection framing for extreme imbalance.

**Follow-up / Key points:**
- SMOTE generates synthetic minority samples (interpolation), better than naive duplication.
- Apply resampling only on training data, never on the test set.

---

## SECTION 4 - DEEP LEARNING

### Q29. What is a neural network / perceptron?
**A:** A perceptron is a single neuron: it computes a weighted sum of inputs plus a bias, then applies an activation function. A neural network stacks layers of such neurons (input, hidden, output); each connection has a learnable weight. With non-linear activations and enough neurons, it can approximate complex non-linear functions (universal approximation).

**Follow-up / Key points:**
- Depth lets it learn hierarchical features.
- Without non-linear activation, any depth collapses to a single linear layer.

### Q30. Why do we need activation functions? Name a few.
**A:** Activation functions introduce non-linearity, letting the network learn complex patterns; without them the whole network is just a linear model. Common ones: ReLU (max(0,x), default for hidden layers), Sigmoid (0-1, for binary output), Tanh (-1 to 1), Softmax (multiclass output probabilities), Leaky ReLU (fixes dying ReLU).

**Follow-up / Key points:**
- ReLU: fast, avoids vanishing gradient, but neurons can "die".
- Sigmoid/Tanh: saturate and cause vanishing gradients in deep nets.

### Q31. Explain backpropagation.
**A:** Backpropagation is how neural networks learn. It does a forward pass to compute the output and loss, then propagates the error backward layer by layer using the chain rule to compute the gradient of the loss with respect to every weight. An optimizer (e.g. gradient descent) then updates weights in the direction that reduces the loss.

**Follow-up / Key points:**
- It is just the chain rule applied efficiently.
- Forward pass = predict; backward pass = assign blame to weights.

### Q32. Gradient descent and its variants (SGD, mini-batch, Adam).
**A:** Gradient descent updates weights opposite to the gradient of the loss, scaled by the learning rate. Batch GD uses the whole dataset per step (slow, stable). SGD uses one sample (fast, noisy). Mini-batch uses a small batch (the practical default). Adam adds momentum and per-parameter adaptive learning rates, usually converging faster and more reliably.

**Follow-up / Key points:**
- Momentum: accelerates in consistent directions, dampens oscillation.
- Adam = momentum + RMSProp; great default optimizer.
- Learning rate is the most important hyperparameter.

### Q33. What are vanishing and exploding gradients?
**A:** In deep networks, gradients are products of many terms during backprop. If terms are < 1, gradients shrink toward zero (vanishing) and early layers stop learning; if > 1, they blow up (exploding) and training diverges. Vanishing is common with sigmoid/tanh.

**Follow-up / Key points:**
- Fixes: ReLU activations, proper weight init (He/Xavier), batch normalization, residual connections, gradient clipping (for exploding), LSTM/GRU gates (for RNNs).

### Q34. What is batch normalization?
**A:** Batch normalization normalizes the inputs of each layer (zero mean, unit variance) per mini-batch, then scales and shifts with learnable parameters. It stabilizes and speeds up training, allows higher learning rates, reduces sensitivity to initialization, and has a mild regularizing effect.

**Follow-up / Key points:**
- Reduces internal covariate shift.
- Behaves differently in train vs inference (uses running statistics at inference).

### Q35. What is dropout?
**A:** Dropout is a regularization technique that randomly "drops" (sets to zero) a fraction of neurons during each training step, forcing the network not to rely on any single neuron and to learn redundant, robust features. At inference all neurons are active (scaled accordingly).

**Follow-up / Key points:**
- Typical rate 0.2-0.5.
- Only active during training.

### Q36. What is a CNN and why is it good for images?
**A:** A Convolutional Neural Network uses convolutional layers that slide learnable filters over the input to detect local patterns (edges, textures, then shapes). Key ideas: parameter sharing (same filter across the image) and local receptive fields make it efficient and translation-invariant. Pooling layers downsample to reduce dimensions and add invariance.

**Follow-up / Key points:**
- Hierarchy: early layers learn edges, deeper layers learn objects.
- Far fewer parameters than a fully connected net on images.
- Components: convolution, ReLU, pooling, fully connected head.

### Q37. What are RNNs, and why LSTM/GRU?
**A:** Recurrent Neural Networks process sequences by maintaining a hidden state passed step to step, so they capture temporal dependencies. Plain RNNs suffer vanishing gradients and forget long-range context. LSTMs add gates (input, forget, output) and a cell state to control information flow, and GRUs are a lighter version with fewer gates - both handle long-term dependencies much better.

**Follow-up / Key points:**
- LSTM: 3 gates + cell state; GRU: 2 gates, faster, fewer parameters.
- Largely superseded by Transformers for NLP, but still used for some time-series.

### Q38. How do you choose the number of layers / neurons?
**A:** There is no fixed formula - it is empirical. Start with a known architecture or a small network, then increase capacity until you can overfit, and then regularize. Use validation performance to guide it, along with techniques like early stopping and hyperparameter search.

**Follow-up / Key points:**
- More capacity needs more data and regularization.
- Transfer learning often beats designing from scratch.

### Q39. What is transfer learning?
**A:** Transfer learning reuses a model pretrained on a large dataset (e.g. ImageNet, or a large text corpus) and adapts it to a new, related task with much less data. You typically freeze early layers (general features) and fine-tune later layers (task-specific). It saves compute and works well when labelled data is limited.

**Follow-up / Key points:**
- Feature extraction (freeze backbone) vs fine-tuning (update some/all layers).
- Foundation of modern CV and NLP.

---

## SECTION 5 - NLP & TRANSFORMERS

### Q40. What is tokenization?
**A:** Tokenization breaks text into smaller units (tokens) the model can process - words, subwords, or characters. Modern models use subword tokenization (BPE, WordPiece, SentencePiece) which balances vocabulary size and the ability to handle rare/unknown words by splitting them into known pieces.

**Follow-up / Key points:**
- Subword handles out-of-vocabulary words gracefully.
- Token count drives cost and context-window limits in LLMs.

### Q41. What are word embeddings (Word2Vec, GloVe)?
**A:** Embeddings represent words as dense vectors in a continuous space where semantically similar words are close together. Word2Vec learns them by predicting context (Skip-gram) or the word from context (CBOW). GloVe learns them from global word co-occurrence statistics. They capture meaning and analogies (king - man + woman ~ queen).

**Follow-up / Key points:**
- These are static - one vector per word regardless of context.
- Contextual embeddings (BERT) give different vectors per usage - a big improvement.

### Q42. Explain the attention mechanism.
**A:** Attention lets a model weigh the relevance of every other token when encoding a given token, instead of relying on a fixed-size summary. Each token produces Query, Key, and Value vectors; attention scores come from Query-Key dot products (scaled and softmaxed), and the output is the weighted sum of Values. This captures long-range dependencies directly.

**Follow-up / Key points:**
- Self-attention: tokens attend to other tokens in the same sequence.
- Formula: softmax(QK^T / sqrt(d_k)) V.
- Multi-head attention runs several attentions in parallel to capture different relationships.

### Q43. Explain the Transformer architecture.
**A:** The Transformer is built on self-attention and processes all tokens in parallel (unlike RNNs). It has an encoder (stacks of multi-head self-attention + feed-forward layers) and a decoder (adds masked self-attention + cross-attention to the encoder). Positional encodings inject word order. Residual connections and layer norm stabilize training.

**Follow-up / Key points:**
- "Attention Is All You Need" (2017).
- Parallelizable = scales to huge data/models, unlike sequential RNNs.
- Encoder-only (BERT), decoder-only (GPT), encoder-decoder (T5, original Transformer).

### Q44. BERT vs GPT - what is the difference?
**A:** BERT is encoder-only and bidirectional - it sees the whole sentence at once, trained with masked language modelling (predict masked words). It is great for understanding tasks (classification, NER, QA). GPT is decoder-only and autoregressive - it predicts the next token left to right, trained on next-word prediction. It is great for generation.

**Follow-up / Key points:**
- BERT: understanding/embeddings; GPT: generation.
- BERT trained with MLM + (originally) next-sentence prediction.
- GPT scales to the modern LLMs.

### Q45. Why did Transformers replace RNNs/LSTMs?
**A:** RNNs process tokens sequentially, which is slow and struggles with long-range dependencies due to vanishing gradients. Transformers process all tokens in parallel via self-attention, capture long-range dependencies directly, train far faster on modern hardware, and scale to massive datasets and parameter counts.

**Follow-up / Key points:**
- Parallelism + scalability is the key win.
- Cost: attention is O(n^2) in sequence length.

---

## SECTION 6 - GENERATIVE AI / LLMs

### Q46. How does a large language model (LLM) work at a high level?
**A:** An LLM is a Transformer (usually decoder-only) trained on huge text corpora to predict the next token given previous tokens. By learning statistical patterns of language at scale, it can generate coherent text, answer questions, summarize, translate, and reason to a degree. It is trained self-supervised - the "label" is just the next word in the text.

**Follow-up / Key points:**
- Core objective: next-token prediction.
- Emergent abilities appear with scale (parameters + data + compute).

### Q47. Explain pretraining vs fine-tuning.
**A:** Pretraining trains the model from scratch on a massive general corpus to learn language broadly - expensive, done once. Fine-tuning takes that pretrained model and trains it further on a smaller, task- or domain-specific dataset to specialize it. Fine-tuning is cheaper and needs far less data because the model already "knows" language.

**Follow-up / Key points:**
- Instruction tuning + RLHF align a base model to follow instructions helpfully.
- PEFT methods like LoRA fine-tune only a small set of added parameters - cheap and efficient.

### Q48. What is RAG (Retrieval-Augmented Generation)?
**A:** RAG augments an LLM with external knowledge at inference time. The user query is embedded and used to retrieve relevant documents from a vector database; those documents are injected into the prompt as context, and the LLM generates an answer grounded in them. It reduces hallucination and lets the model use up-to-date or private data without retraining.

**Follow-up / Key points:**
- Pipeline: chunk docs -> embed -> store in vector DB -> retrieve top-k by similarity -> augment prompt -> generate.
- Solves knowledge cutoff and lets you cite sources.
- Quality depends heavily on chunking and retrieval quality.

### Q49. What are embeddings and vector databases in the LLM context?
**A:** Embeddings convert text (or images) into dense vectors capturing semantic meaning, so similar content is nearby in vector space. A vector database stores these and enables fast similarity search (cosine/dot-product, often via approximate nearest-neighbour indexes). They power semantic search, RAG, and recommendations.

**Follow-up / Key points:**
- Similarity: cosine similarity is most common.
- Examples: Pinecone, Weaviate, FAISS, Chroma, pgvector.
- ANN (HNSW) trades a little accuracy for big speed at scale.

### Q50. What are hallucinations and how do you reduce them?
**A:** A hallucination is when an LLM produces fluent but factually wrong or fabricated content, because it predicts plausible text rather than retrieving verified facts. Reduce with RAG (ground answers in real sources), better prompting (ask it to say "I don't know", to cite), lower temperature, fine-tuning on domain data, and output validation / guardrails.

**Follow-up / Key points:**
- Root cause: next-token prediction has no built-in notion of truth.
- "Grounding" via retrieval is the most effective mitigation.

### Q51. What is the context window?
**A:** The context window is the maximum number of tokens (input + output) a model can consider at once. Anything beyond it is truncated or forgotten. It limits how much document/conversation history you can feed in a single call and is a key reason for techniques like RAG, chunking, and summarization.

**Follow-up / Key points:**
- Larger windows cost more (attention is O(n^2)).
- Token != word (~0.75 words per token in English).

### Q52. What does temperature do? Top-k / top-p?
**A:** Temperature controls randomness in generation by scaling the logits before sampling. Low temperature (near 0) makes output deterministic and focused; high temperature makes it diverse and creative. Top-k samples from the k most likely tokens; top-p (nucleus) samples from the smallest set of tokens whose cumulative probability exceeds p.

**Follow-up / Key points:**
- Factual tasks: low temperature. Creative tasks: higher.
- Top-p adapts the candidate set dynamically; top-k is fixed size.

### Q53. What is prompt engineering? Zero-shot vs few-shot?
**A:** Prompt engineering is crafting inputs to steer an LLM toward better outputs. Zero-shot gives only the instruction; few-shot includes a few examples in the prompt to show the desired format/behaviour. Chain-of-thought prompting asks the model to reason step by step, improving performance on complex/multi-step tasks.

**Follow-up / Key points:**
- Be specific, give role/context, specify output format, give examples.
- Few-shot uses in-context learning - no weight updates.

### Q54. What is fine-tuning vs RAG vs prompt engineering - when to use which?
**A:** Prompt engineering is the cheapest, first thing to try - no training, fast iteration. RAG is best when you need the model grounded in external, changing, or private knowledge. Fine-tuning is best when you need to change behaviour/style/format consistently or teach a specialized task, and you have quality training data. They are complementary, not mutually exclusive.

**Follow-up / Key points:**
- Order of preference usually: prompt -> RAG -> fine-tune.
- RAG = knowledge problem; fine-tuning = behaviour/skill problem.

### Q55. What is RLHF?
**A:** Reinforcement Learning from Human Feedback aligns an LLM with human preferences. Humans rank model outputs; those rankings train a reward model; then the LLM is fine-tuned with reinforcement learning (e.g. PPO) to maximise that reward. This is what makes base models helpful, harmless, and good at following instructions.

**Follow-up / Key points:**
- Three stages: supervised fine-tuning -> reward model -> RL optimization.
- Turns a raw next-token predictor into a useful assistant.

---

## QUICK-FIRE RAPID REVISION

- **Generative vs Discriminative:** Generative models the joint P(x,y) and can generate data (Naive Bayes, GANs, LLMs); discriminative models P(y|x), the decision boundary (logistic regression, SVM).
- **Parametric vs non-parametric:** Parametric has a fixed number of parameters (linear/logistic regression); non-parametric grows with data (KNN, decision trees).
- **Generalization:** how well a model performs on unseen data - the whole point of ML.
- **Hyperparameter vs parameter:** parameters are learned from data (weights); hyperparameters are set before training (learning rate, k, max_depth).
- **Epoch vs batch vs iteration:** epoch = one full pass over data; batch = subset per update; iteration = one weight update.
- **Loss vs metric:** loss is what the model optimizes (must be differentiable, e.g. cross-entropy); metric is what you report (e.g. accuracy, F1).
- **Ensemble:** combine multiple models to beat any single one (bagging, boosting, stacking).
- **One-hot vs embedding:** one-hot is sparse and dimension-heavy; embeddings are dense, learned, and capture similarity.

---

## One-Line Definitions

* **Supervised Learning** → learns from labelled input-output pairs.
* **Unsupervised Learning** → finds structure in unlabelled data.
* **Reinforcement Learning** → agent learns by maximising reward through trial and error.
* **Bias** → error from overly simple assumptions (underfitting).
* **Variance** → error from sensitivity to training data (overfitting).
* **Overfitting** → fits training noise, fails on unseen data.
* **Underfitting** → too simple to capture the pattern.
* **Regularization** → penalty on weights to reduce overfitting.
* **L1 (Lasso)** → drives weights to zero, does feature selection.
* **L2 (Ridge)** → shrinks weights smoothly, handles correlated features.
* **Cross-Validation** → rotate train/validation folds for reliable scoring.
* **Data Leakage** → outside/future info sneaks into training, inflating scores.
* **Curse of Dimensionality** → data gets sparse as features grow.
* **Feature Scaling** → put features on a comparable range (standardize/normalize).
* **One-Hot Encoding** → one binary column per category.
* **Linear Regression** → fits a linear mapping by minimising MSE.
* **Logistic Regression** → sigmoid on a linear model for classification.
* **Decision Tree** → recursive threshold splits on impurity (Gini/entropy).
* **Random Forest** → bagged ensemble of decorrelated trees.
* **Bagging** → parallel models on bootstraps, reduces variance.
* **Boosting** → sequential models fixing prior errors, reduces bias.
* **XGBoost** → optimized regularized gradient boosting for tabular data.
* **SVM** → maximum-margin classifier; kernel trick for non-linear data.
* **KNN** → predicts from the k nearest training points (lazy learner).
* **Naive Bayes** → Bayes' theorem assuming feature independence.
* **K-Means** → partitions data into k clusters by minimising within-cluster variance.
* **DBSCAN** → density-based clustering that finds outliers, no k needed.
* **PCA** → projects data onto directions of maximum variance.
* **Confusion Matrix** → table of TP, FP, TN, FN.
* **Precision** → of predicted positives, how many are correct.
* **Recall** → of actual positives, how many were caught.
* **F1 Score** → harmonic mean of precision and recall.
* **ROC-AUC** → threshold-independent measure of ranking quality.
* **SMOTE** → generates synthetic minority samples for imbalance.
* **Perceptron** → single neuron: weighted sum plus activation.
* **Activation Function** → adds non-linearity (ReLU, sigmoid, tanh, softmax).
* **Backpropagation** → chain rule to compute weight gradients from loss.
* **Gradient Descent** → updates weights opposite to the loss gradient.
* **Adam** → adaptive optimizer combining momentum and RMSProp.
* **Vanishing Gradient** → gradients shrink to zero, early layers stop learning.
* **Batch Normalization** → normalizes layer inputs to stabilize training.
* **Dropout** → randomly drops neurons during training to regularize.
* **CNN** → uses convolution filters to detect local patterns in images.
* **RNN** → processes sequences via a hidden state passed step to step.
* **LSTM/GRU** → gated RNNs that handle long-range dependencies.
* **Transfer Learning** → reuse a pretrained model on a new related task.
* **Tokenization** → splits text into tokens (words/subwords).
* **Word Embedding** → dense vector capturing word meaning.
* **Attention** → weighs relevance of all tokens via Query-Key-Value.
* **Transformer** → parallel self-attention architecture, no recurrence.
* **BERT** → bidirectional encoder for understanding tasks.
* **GPT** → autoregressive decoder for text generation.
* **LLM** → large Transformer trained to predict the next token.
* **Pretraining** → train from scratch on a massive general corpus.
* **Fine-Tuning** → adapt a pretrained model to a specific task.
* **RAG** → retrieve external documents to ground LLM answers.
* **Vector Database** → stores embeddings for fast similarity search.
* **Hallucination** → fluent but factually wrong LLM output.
* **Context Window** → max tokens a model can process at once.
* **Temperature** → controls randomness of LLM generation.
* **Prompt Engineering** → crafting inputs to steer LLM output.
* **RLHF** → aligns LLMs to human preferences via a reward model.

---

*End of master revision. Good luck in the mock.*
