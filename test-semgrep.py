#To test with the backid in dev -> 687107cf93259d2193e951fd

from django.dispatch import Signal

# Define a custom signal
my_signal = Signal()

# Define a dummy receiver
def handle_custom_signal(sender, **kwargs):
    print("Custom signal received.")

# Connect the signal
my_signal.connect(handle_custom_signal)

print("Something")
print("new changes for feature branch")


# 🚫 This line violates the rule: using the 'weak' argument
my_signal.disconnect(handle_custom_signal, weak=False)
