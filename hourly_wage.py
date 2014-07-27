r"""
The functions below compute gross earnings from net earnings subject to
New Zealand income tax rates for April 2014 to March 2015.

AUTHORS:

- Alex Raichev (2013-03-19)
"""
from scipy.optimize import brentq

# April 2014 to March 2015 New Zealand income tax tiers for individuals 
# and their corresponding tax rates.
NZ_TAX_TIERS_2014 = [
  (14000, 0.105), 
  (48000, 0.175), 
  (70000, 0.3), 
  (10e12, 0.33)
]
WORK_WEEKS_PER_YEAR = 47 # Considering 4 weeks annual leave and holidays

def tax(gross_yearly_income, tax_tiers=NZ_TAX_TIERS_2014, ndigits=2):
    r"""
    Return the income tax due and the effective tax rate on the given 
    gross yearly income.    
    Use the given tax tiers and round results to `ndigits` decimal places.
    Assume `gross_yearly_income >= 1`.

    EXAMPLES::

        >>> print(tax(13999, ndigits=3))
        (1469.895, 0.105)
        >>> print(tax(14000, ndigits=3))
        (1470.0, 0.105)
        >>> print(tax(15000, ndigits=3))
        (1645.0, 0.11)
        >>> print(tax(65238))
        (12591.4, 0.19)
        >>> print(tax(45000))
        (6895.0, 0.15)
    """
    gyi = gross_yearly_income
    # Ensure good input.
    if gyi < 1:
        gyi = 1
    result = 0.0
    previous_cutoff = 0
    for (cutoff, tax_rate) in tax_tiers:
        if gyi < cutoff:
            result += (gyi - previous_cutoff)*tax_rate
            break
        else:
            result += (cutoff - previous_cutoff)*tax_rate
        previous_cutoff = cutoff
    return round(result, ndigits), round(result/gyi, ndigits)

def tax_h(gross_hourly_income, hours_per_week, 
  work_weeks_per_year=WORK_WEEKS_PER_YEAR, tax_tiers=NZ_TAX_TIERS_2014,
  ndigits=2):
    r"""
    Return the income tax due and the effective tax rate on the 
    gross yearly income `gross_hourly_income*hours_per_week*weeks_per_year`.
    Use the given tax tiers and round all results to `ndigits` decimal  
    places.

    EXAMPLES::

        >>> print(tax_h(75, 20))
        (14185.0, 0.2)
    """
    gyi = gross_hourly_income*hours_per_week*work_weeks_per_year
    return tax(gyi, tax_tiers=tax_tiers, ndigits=ndigits)

def gross_yearly_income(net_yearly_income, tax_tiers=NZ_TAX_TIERS_2014, 
  ndigits=2):
    r"""
    Return the gross yearly income required to earn the given   
    net yearly income after subtracting income tax specified by the given 
    tax tiers.
    Round result to `ndigits` decimal places.
    
    EXAMPLES::
    
        >>> nyi = 50000
        >>> gyi = gross_yearly_income(nyi)
        >>> print(gyi)
        61457.14
        >>> nyi_get = gyi - tax(gyi)[0]
        >>> print(nyi, nyi_get)
        50000 50000.0
    """                    
    def f(y):
        return y - tax(y, tax_tiers=tax_tiers)[0] - net_yearly_income
    # The gross yearly income is the zero of f.
    gyi = brentq(f, 1, 1e9)  
    return round(gyi, ndigits)

def gross_hourly_income(net_weekly_income, hours_per_week, 
  work_weeks_per_year=WORK_WEEKS_PER_YEAR, tax_tiers=NZ_TAX_TIERS_2014,
  ndigits=2):
    r"""
    Return the gross hourly income required to earn the given net weekly 
    income (for 52 weeks per year) when working the given number of hours 
    per week for the given number of weeks per year after subtracting income
    tax specified by the given tax tiers.
    Round result to `ndigits` decimal places.

    EXAMPLES::

        >>> net_weekly_income = 1200
        >>> hours_per_week = 20
        >>> weeks_per_year = 47
        >>> ghi = gross_hourly_income(net_weekly_income, hours_per_week, weeks_per_year) 
        >>> print(ghi)
        84.66
        >>> gyi = ghi*hours_per_week*weeks_per_year
        >>> tax, tax_rate = tax(gyi)
        >>> nyi = gyi - tax
        >>> net_weekly_income_get = round(nyi/52, 2)
        >>> print(net_weekly_income, net_weekly_income_get)
        1200 1199.98
        >>> print(tax_rate, tax_h(ghi, hours_per_week)[1])
        0.22 0.22
    """    
    gyi = gross_yearly_income(net_weekly_income*52)
    ghi = gyi/(hours_per_week*work_weeks_per_year)
    return round(ghi, ndigits)

HOURS = [5*i for i in range(1, 9)]
NET_WEEKLY_INCOMES = [100*i for i in range(1, 26)]

def max_len(items):
    """
    Return the length of the longest item (when converted to a string) 
    in the given list.
    """
    return max(len(str(item)) for item in items)

def print_table(hours=HOURS, net_weekly_incomes=NET_WEEKLY_INCOMES):
    # import pandas as pd
    #
    # nwis = [(x, 52*x) for x in net_weekly_incomes]
    # nwis_str = [('$' + str(nwi[0]), '$' + str(nwi[1])) for nwi in nwis]
    # data = [[ '$' + str(int(gross_hourly_income(nwi[0], hour))) 
    #         for hour in hours] for nwi in nwis]
    # df = pd.DataFrame(data, index=nwis_str, columns=hours)
    # print(textwrap.dedent("""
    #   Gross hourly income given
    #   net (weekly, yearly) income for 52 weeks per year and
    #   hours worked per week for 47 weeks per year
    #   -------------------------------------------------------"""))
    # print(df)

    # Print without Pandas to reduce third-party module dependecies. 
    import textwrap
    
    # Create the table
    nwis = net_weekly_incomes
    col_header = [' '] + [str(h) for h in hours]
    table = [['($%s, $%s)' % (nwi, 52*nwi)] +\
            [ '$' + str(int(gross_hourly_income(nwi, hour))) 
            for hour in hours] for nwi in nwis]
    table = [col_header] + table
    nrows = len(table)
    ncols = len(table[0])

    # Compute right justification amounts for each column.
    # Left pad each column except the firsts by 2 spaces.
    col_rjusts = [max_len([table[i][0] for i in range(nrows)])]
    col_rjusts.extend(  
      [max_len([table[i][j] for i in range(nrows)]) + 2
       for j in range(1, ncols)]
    )

    # Print the table
    print(textwrap.dedent("""\
      +-------------------------------------------------------+
      | Gross hourly income given                             |
      | net (weekly, yearly) income for 52 weeks per year and |
      | hours worked per week for %s weeks per year           |
      +-------------------------------------------------------+""" %\
      WORK_WEEKS_PER_YEAR))
    for i in range(nrows):
        for j in range(ncols):
            print(table[i][j].rjust(col_rjusts[j]), end='')
        print() 

if __name__ == '__main__':
    print_table()