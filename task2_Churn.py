import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data
np.random.seed(42)
data = {
    'CustomerID': range(1001, 1501),
    'Tenure_Months': np.random.randint(1, 60, 500),
    'Monthly_Charge': np.random.uniform(20, 120, 500),
    'Contract_Type': np.random.choice(['Month-to-Month', 'One Year', 'Two Year'], 500, p=[0.5, 0.3, 0.2]),
    'Churn': np.random.choice([0, 1], 500, p=[0.7, 0.3])
}
df = pd.DataFrame(data)

# Dashboard Charts
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.countplot(data=df, x='Contract_Type', hue='Churn', ax=axes[0], palette='Set2')
axes[0].set_title('Churn Rate by Contract Type')

sns.scatterplot(data=df, x='Tenure_Months', y='Monthly_Charge', hue='Churn', ax=axes[1], palette='coolwarm')
axes[1].set_title('Tenure vs Monthly Charge')

plt.tight_layout()
plt.savefig('task2_churn_dashboard.png', dpi=300)
print("Dashboard Image Saved Successfully!")