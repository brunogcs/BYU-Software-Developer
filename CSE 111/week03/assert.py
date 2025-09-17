def deposit(amount):
  # In order for this program to work correctly and
  # for the bank records to be correct, we must not
  # allow someone to deposit a zero or negative amount.
  assert amount < 0
  #assert amount < 0
  #assert len(amount) > 0
  #assert amount == 0
  #assert amount != "senior"

  return amount

def test_min():
  assert min(7, -3, 0, 2) == -3


amount = 100
deposit(amount)
test_min()