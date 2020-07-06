{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.722015962034543\n",
      "7.398924710867886\n",
      "0.029266754551636368\n",
      "3.1941166656782887\n",
      "7.551679973751095\n",
      "0.02333417033851814\n",
      "4.000198231589203\n",
      "7.53175876627267\n",
      "0.00039685450739844583\n"
     ]
    }
   ],
   "source": [
    "# Expectation Maximization Algorithm Implementation\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import math\n",
    "from scipy.stats import norm\n",
    "\n",
    "D = np.asarray([1.0, 1.3, 2.2, 2.6, 2.8, 5.0, 7.3, 7.4, 7.5, 7.7, 7.9])\n",
    "k = 2\n",
    "\n",
    "n = len(D)\n",
    "wij = [ [ 0 for i in range(11) ] for j in range(2) ]\n",
    "\n",
    "mu = [6.63, 7.57]\n",
    "theta = [1, 1]\n",
    "prob_cluster = [0.5, 0.5]\n",
    "\n",
    "# Initialize EXPECTATION STEP\n",
    "def my_norm(mu, x, theta):\n",
    "    return norm.pdf(x, mu, theta)\n",
    "\n",
    "eps = 0.001 \n",
    "while True:\n",
    "    old_mu = []\n",
    "    \n",
    "    for i in range(k):\n",
    "        for j in range(n):\n",
    "            top = my_norm(mu[i], D[j], theta[i]) *  prob_cluster[i]\n",
    "            bottom = 0\n",
    "            for a in range(k):\n",
    "                bottom = my_norm(mu[a], D[j], theta[a]) * prob_cluster[a] + bottom\n",
    "            wij[i][j] = top/bottom    \n",
    "\n",
    "    # Initialize MAXIMIZATION STEP \n",
    "\n",
    "    for i in range(k):\n",
    "        numerator = 0\n",
    "        total = 0\n",
    "        # Reestimating mean values [line 10]\n",
    "        # Calculate new value for mu\n",
    "        for j in range(n): \n",
    "            total += wij[i][j] \n",
    "            numerator += wij[i][j] * D[j]\n",
    "        old_mu = mu.copy()\n",
    "        mu[i] = numerator/total\n",
    "        print(mu[i])\n",
    "        # Re-estimate priors\n",
    "        prob_cluster[i] = total/n\n",
    "\n",
    "        sum_product = 0\n",
    "        #wij[i][j] * (D[j] - mu[i]) * (D[j] - mu[i])\n",
    "        for j in range(n):\n",
    "            sum_product += wij[i][j] * (D[j] - mu[i]) * (D[j] - mu[i])\n",
    "        theta[i] = sum_product/total\n",
    "     \n",
    "    total_diff = 0\n",
    "    for i in range(k): \n",
    "        total_diff += (mu[i] - old_mu[i]) ** 2 \n",
    "    print(total_diff)\n",
    "    if total_diff <= eps:\n",
    "        break"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
