# 📊 Spread Locator: Statistical Distribution Analysis Model

## 📌 Project Overview

This project analyzes customer transaction data using statistical
distributions and probability modeling techniques to derive meaningful
business insights.

------------------------------------------------------------------------

## 🎯 Objectives

-   Understand probability distributions
-   Model transaction behaviors
-   Identify best-fit distributions
-   Apply statistical transformations
-   Compute probabilities and risk metrics

------------------------------------------------------------------------

## 📂 Dataset Fields

-   transaction_id
-   customer_id
-   transaction_amount
-   transaction_date
-   transaction_count
-   region
-   transaction_status

------------------------------------------------------------------------

## 📊 Distributions Applied

  Variable             Distribution
  -------------------- --------------
  Success/Fail         Bernoulli
  Weekly Count         Binomial
  Daily Count          Poisson
  Transaction Amount   Log-Normal

------------------------------------------------------------------------

## 🔬 Techniques Used

-   Q-Q Plot for normality testing
-   Box-Cox Transformation
-   Z-score calculation
-   PDF & CDF plotting
-   Distribution fitting using SciPy

------------------------------------------------------------------------

## 📈 Key Insights

-   Transaction amounts are right-skewed.
-   Log-Normal distribution provides best fit.
-   Probability of high-value transactions (\> ₹5000) helps in risk
    modeling.
-   Statistical modeling supports fraud detection and premium customer
    targeting.

------------------------------------------------------------------------

## 🛠 Tools Used

-   Python
-   NumPy
-   Pandas
-   SciPy
-   Matplotlib
-   Seaborn

------------------------------------------------------------------------

## 📌 Conclusion

Statistical distribution modeling enhances understanding of transaction
spread and supports data-driven decision making.

------------------------------------------------------------------------
