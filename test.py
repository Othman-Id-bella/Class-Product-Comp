from test import Composition , Produit, Elementaire ,Compose

p1 = Elementaire("P1", "001",10)
p2 = Elementaire("P2", "002",15)

print(p1.__str__())
comp_p3 = Composition(p1, 2)
comp_p4 = Composition(p2, 3)
comp_p4_2 = Composition(p1, 2)

p3 = Compose("P3", "003", 5.0, [comp_p3, comp_p4_2])
p4 = Compose("P4", "004", 8.0, [comp_p4, comp_p3])

print("Prix HT de P3:", p3.getPrixHT())
print("Prix HT de P4: ",p4.getPrixHT())
