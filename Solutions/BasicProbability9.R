a <-  1/12
b <- 1/10
c <- 1/15
library(MASS)

accepted_in_one <- a*(1-b)*(1-c) + (1-a)*b*(1-c) + (1-a)*(1-b)*c
accepted_in_two <- a*b*(1-c) + a*(1-b)*c + (1-a)*b*c
accepted_in_three <- a*b*c
as.fractions(accepted_in_one+
               accepted_in_two+
               accepted_in_three)

bill <- 1/3
nina <- 1/5
(bill)*(1-nina) + (1-bill)*nina


 (64.71 / 4) + (124.51 / 4) + (259.47 / 5) + (30.05 / 3) -(55.58 / 5)

kks