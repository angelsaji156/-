# exp 2
import numpy as np
import matplotlib.pyplot as plt

# Generate random bits
bits = np.random.randint(0, 2, 10)
print("Bits:", bits)

# Convert bits to signals (0 -> -1, 1 -> +1)
signal = 2 * bits - 1
print("Signal:", signal)

# Add noise
noise = np.random.normal(0, 0.5, 10)
received_signal = signal + noise
print("Received Signal:", received_signal)

# Plot
plt.figure(figsize=(8, 4))
plt.plot(signal, 'bo-', label='Transmitted Signal')
plt.plot(received_signal, 'r*-', label='Received Signal')
plt.title("Basic Wireless Communication System")
plt.xlabel("Bit Number")
plt.ylabel("Signal Amplitude")
plt.grid(True)
plt.legend()
plt.show()