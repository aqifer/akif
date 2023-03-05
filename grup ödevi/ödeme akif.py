print("hello world")

#salffev/cemal akif özateş

import stripe

# Stripe API anahtarını tanımlayın
stripe.api_key = "sk_test_1234567890abcdefghijklmnopqrs"

# Ödeme işlemi için müşteri ve kart bilgilerini belirleyin
customer = stripe.Customer.create(email="test@example.com")
card = stripe.Customer.create_source(customer.id, source="tok_visa")

# Ödeme işlemi için gerekli parametreleri belirleyin
charge = stripe.Charge.create(
    amount=2000,
    currency="türk lirasi",
    customer=customer.id,
    source=card.id,
    description="Test payment"
)

# Ödeme işlemi sonucunu kontrol edin
if charge.status == "succeeded":
    print("Payment succeeded!")
else:
    print("Payment failed.")
