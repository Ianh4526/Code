import numpy as np

np.random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalsPurchases = 0

for _ in range(100000):
    ageDecade = np.random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = 0.4
    totals[ageDecade] += 1
    if (np.random.random() < purchaseProbability):
        totalsPurchases +=1
        purchases[ageDecade] +=1

print "\nTOTALS"
print totals

print "\nPURCHASES"
print purchases

print "\nTOTAL PURCHASES"
print totalsPurchases

# P(E|F)
#E is purchases
#F is you are on your 30s
PEF = float(purchases[30]) / float(totals[30])
print "\nP(purchases | 30s):"
print PEF

#P(F)
#probability of being 30
PF = float(totals[30]) / 100000.0
print "\nP(30s):"
print PF

#P(E)
#probabilityof buying something
PE = float(totalsPurchases) / 100000.0
print "\nP(Purchase):"
print PE

#if E and F where independent the P(E|F) = P(E) but the are not
print "\nP(30s)P(Purchase):"
print PE*PF

#probability of E and F together
#P(E,F) = P(E) * P(F)
print "\nP(30s, Purchase):"
print float(purchases[30])/100000.0

#P(E|F) = P(E,F)/P(F)
print "\nP(E,F)/P(F):"
print  (float(purchases[30])/100000.0) /PF
