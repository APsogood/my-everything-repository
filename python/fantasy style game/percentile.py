import matplotlib.pyplot as plt
import numpy as np

scores = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

# Calculate percentiles
p25, p50, p75 = np.percentile(scores, [25, 50, 75])

# Create plot
plt.figure(figsize=(8,4))
plt.scatter(scores, [1]*len(scores), alpha=0.5)  # Plot scores
plt.yticks([])  # Hide y-axis
plt.xlabel('Test Scores')

# Add percentile lines
plt.axvline(p25, color='r', linestyle='--', label=f'25th %ile ({p25})')
plt.axvline(p50, color='g', linestyle='-', label=f'50th %ile ({p50})')
plt.axvline(p75, color='b', linestyle='--', label=f'75th %ile ({p75})')

plt.legend()
plt.title('Test Score Percentiles')
plt.show()