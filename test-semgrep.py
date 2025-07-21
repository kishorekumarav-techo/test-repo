#To test with the backid in dev -> 687107cf93259d2193e951fd

from django.dispatch import Signal

# Define a custom signal
my_signal = Signal()

# Define a dummy receiver
def log_custom_signal_receipt(sender, **kwargs):
    print("Custom signal received.")

# Connect the signal
my_signal.connect(log_custom_signal_receipt)

print("Something")
print("new changes for feature branch")


# 🚫 This line violates the rule: using the 'weak' argument
my_signal.disconnect(log_custom_signal_receipt, weak=False)
