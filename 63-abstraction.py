# Abstraction
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class CreditCardPayment(Payment):
    def process_payment(self):
        # Code to process Credit Card payment
        pass


class StripePayment(Payment):
    def process_payment(self):
        # Code to process Stripe payment
        pass


class PayPalPayment(Payment):
    def process_payment(self):
        # Code to process PayPal payment
        pass
