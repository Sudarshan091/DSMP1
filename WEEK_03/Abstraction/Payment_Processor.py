"""Imagine you are building an e-commerce app. You need a way to process payments, but
 the way a CreditCard handles a transaction is totally different from how PayPal does it.

Requirements:

Abstract Base Class: Create a class PaymentProcessor with
 an abstract method called process_payment(amount).

Concrete Class 1: Create a CreditCardProcessor class.
 Its process_payment method should print: "Processing credit card payment of $XX".

Concrete Class 2: Create a PayPalProcessor class.
 Its process_payment method should print: "Processing PayPal payment of $XX".

The Test: Create a list that contains one instance of each processor. 
Loop through that list and call process_payment(100) on each one."""

"""from abc import ABC,abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self):
       pass
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self,amount):
        print("Processing credit card payment of $XX")
class PayPalProcessor(PaymentProcessor):
    def process_payment(self,amount):
        print("Processing PayPal payment of $XX")
trns=CreditCardProcessor()
tr1=PayPalProcessor()
tr1.process_payment(10)
trns.process_payment(100)"""
"""# trns.process_payment(100)
# anount=[100,10000,200,2000]
# for x in amount[0:4]:
#     pass
"""


from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# 1. Create a list of objects
processors = [CreditCardProcessor(), PayPalProcessor()]

# 2. Loop through the list and call the method
# amounts = [100, 500,200,300]

# # Create the processors and the different amounts
# processors = [CreditCardProcessor(), PayPalProcessor()]
# amounts = [100, 500,400,4033]

# # zip() pairs CreditCardProcessor with 100, and PayPalProcessor with 500
# for processor, amount in zip(processors, amounts):
#     processor.process_payment(amount)

# A list of dictionaries containing both the amount and the choice
transactions = [
    {"amount": 100, "method": "credit_card"},
    {"amount": 500, "method": "paypal"},
    {"amount": 400, "method": "credit_card"},
    {"amount": 4033, "method": "paypal"}
]

# Create our processors
cc_processor = CreditCardProcessor()
pp_processor = PayPalProcessor()

# Loop through and use an 'if' statement to route the payment
for tx in transactions:
    if tx["method"] == "credit_card":
        cc_processor.process_payment(tx["amount"])
    elif tx["method"] == "paypal":
        pp_processor.process_payment(tx["amount"])