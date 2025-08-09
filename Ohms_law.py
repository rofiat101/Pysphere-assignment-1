# Voltage Calculator using Ohm's Law
# V = I * R

# Get current (in Amperes) from user
current = float(input("Enter the current (in A): "))

# Get resistance (in Ohms) from user
resistance = float(input("Enter the resistance (in ohms): "))

# Calculate voltage
voltage = current * resistance

# Display result
print(f"The voltage is: {voltage} volts")
