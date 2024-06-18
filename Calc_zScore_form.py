from scipy.stats import norm

# Calculate Z-score for a 95% confidence interval
alpha = 0.05  # Significance level
z_score = norm.ppf(1 - alpha/2)

print("Z-score for a 95% confidence interval:", round(z_score,2))
