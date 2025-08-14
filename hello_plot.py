import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
plt.text(0.5, 0.5, 'Hello, World!', fontsize=20, ha='center', va='center')
plt.axis('off')

# Save instead of show
plt.savefig('hello_world.png')
print("Plot saved as hello_world.png")