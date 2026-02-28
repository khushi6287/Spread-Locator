
"""

**Import Libraries**
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import boxcox

"""**Load Dataset**"""

df = pd.read_csv("transactions.csv")
df.head()

"""# **Fit Bernoulli & Binomial Distribution**

**Bernoulli (Transaction Success)**
"""

df['success'] = df['transaction_status'].apply(lambda x: 1 if x == "Success" else 0)

p = df['success'].mean()
print("Estimated p (Success Probability):", p)

"""**Binomial (Weekly Transaction Count)**"""

mean_weekly = df['transaction_count'].mean()
n = df['transaction_count'].max()
p_binom = mean_weekly / n

print("Estimated n:", n)
print("Estimated p:", p_binom)

x_vals = [0, 1]
pmf_vals = [1 - p, p]
plt.figure()
plt.bar(x_vals, pmf_vals)
plt.title("Bernoulli Distribution")
plt.xlabel("Outcome (0=Fail, 1=Success)")
plt.ylabel("Probability")
plt.show()

"""# **Fit Poisson Distribution**"""

daily_counts = df.groupby('transaction_date').size()
lambda_poisson = daily_counts.mean()

print("Lambda (Average transactions/day):", lambda_poisson)

# Plot comparison
x = np.arange(0, daily_counts.max())
plt.hist(daily_counts, density=True, alpha=0.6)
plt.plot(x, stats.poisson.pmf(x, lambda_poisson))
plt.title("Poisson Fit")
plt.show()

"""# **Model Transaction Amount (Log-Normal & Power Law)**

**Log-Normal Fit**
"""

shape, loc, scale = stats.lognorm.fit(df['transaction_amount'], floc=0)

x = np.linspace(df['transaction_amount'].min(),
                df['transaction_amount'].max(), 100)

pdf_lognorm = stats.lognorm.pdf(x, shape, loc, scale)

plt.hist(df['transaction_amount'], density=True, alpha=0.5)
plt.plot(x, pdf_lognorm)
plt.title("Log-Normal Fit")
plt.show()

"""**Power Law Fit**"""

alpha = stats.powerlaw.fit(df['transaction_amount'])[0]
print("Estimated alpha:", alpha)

"""# **Q-Q Plot**"""

stats.probplot(df['transaction_amount'], dist="norm", plot=plt)
plt.title("Q-Q Plot for Normality")
plt.show()

"""# **Box-Cox Transform**"""

transformed_data, lambda_bc = boxcox(df['transaction_amount'])

print("Lambda:", lambda_bc)

stats.probplot(transformed_data, dist="norm", plot=plt)
plt.title("Q-Q After Box-Cox")
plt.show()

"""# **Calculate Z-Scores & Probability > ₹5000**"""

mean = df['transaction_amount'].mean()
std = df['transaction_amount'].std()

z_5000 = (5000 - mean) / std

prob = 1 - stats.norm.cdf(z_5000)

print("Z-score:", z_5000)
print("Probability > 5000:", prob)

"""#**PDF and CDF**"""

x = np.linspace(mean - 3*std, mean + 3*std, 100)

pdf = stats.norm.pdf(x, mean, std)
cdf = stats.norm.cdf(x, mean, std)

plt.plot(x, pdf)
plt.title("PDF")
plt.show()

plt.plot(x, cdf)
plt.title("CDF")
plt.show()
