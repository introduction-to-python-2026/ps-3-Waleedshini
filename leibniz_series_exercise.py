from fractions import Fraction
def approximate_pi(n_terms):
    list_of_numbers = []
    leibniz_series = []
    for i in range(n_terms):
        list_of_numbers.append(i)
        if i % 2 == 0:
            list_of_numbers[i] = 1
        else:
          list_of_numbers[i] = -1
        leibniz_series.append(Fraction(list_of_numbers[i], (2*i + 1))) 
    pi_approximate = 4* sum(leibniz_series)
    return (pi_approximate)
