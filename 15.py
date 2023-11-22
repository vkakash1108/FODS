import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
np.random.seed(42)  
control_group = np.random.normal(loc=10, scale=2, size=100)
treatment_group = np.random.normal(loc=12, scale=2, size=100)
plt.hist(control_group, alpha=0.5, label='Control Group')
plt.hist(treatment_group, alpha=0.5, label='Treatment Group')
plt.xlabel('Outcome Measurement')
plt.ylabel('Frequency')
plt.legend()
plt.title('Distribution of Outcome Measurement in Control and Treatment Groups')
plt.show()
t_statistic, p_value = stats.ttest_ind(control_group, treatment_group)
print(f'T-statistic: {t_statistic}')
print(f'P-value: {p_value}')
alpha = 0.05
if p_value < alpha:
    print("The difference between the groups is statistically significant.")
else:
    print("There is no significant difference between the groups.")
