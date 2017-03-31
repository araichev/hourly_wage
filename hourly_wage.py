import textwrap

# New Zealand income tax tiers (cutoff value, tax rate) for 2016-04-01 to 2017-03-31
BIG = 10e12
NZ_TAX_TIERS = [
  (14000, 0.105), 
  (48000, 0.175), 
  (70000, 0.3), 
  (BIG, 0.33)
]
# Work weeks per year counting 4 weeks paid leave and 2 weeks paid holiday
WORK_WEEKS_PER_YEAR = 46 


def mindex(x, cutoffs):
    """
    Given a number ``x`` and an increasing list of numbers ``cutoffs``, return the least index i such that such that x < cutoffs[i].
    
    EXAMPLES::

        >>> cutoffs = [14000, 48000, 70000, 10e12]
        >>> mindex(0, cutoffs)
        0
        >>> mindex(14000, cutoffs)
        1
        >>> mindex(70001, cutoffs)
        3
    """
    for i, cutoff in enumerate(cutoffs):
        if x < cutoff:
            break
    return i 

def tax_and_rate(gross_yearly_income, tax_tiers=NZ_TAX_TIERS):
    """
    Return the income tax due and the effective tax rate on the given 
    gross yearly income using the given tax tiers.

    EXAMPLES::

        >>> tax_and_rate(-7)
        (0, 0)
        >>> tax_and_rate(13999)
        (1469.895, 0.105)
        >>> tax_and_rate(14000)
        (1470.0, 0.105)
        >>> tax_and_rate(15000)
        (1645.0, 0.10966666666666666)
        >>> tax_and_rate(85000)
        (18970.0, 0.22317647058823528)
        >>> tax_and_rate(45000)
        (6894.999999999999, 0.1532222222222222)
    """
    x = gross_yearly_income

    if x <= 0:
        return 0, 0

    cutoffs, rates = zip(*tax_tiers)

    # Apply tax formula
    k = mindex(x, cutoffs)
    t = sum([(rates[i] - rates[i + 1])*cutoffs[i] for i in range(k)]) +\
      rates[k]*x

    return t, t/x

def tax_and_rate_h(gross_hourly_income, hours_per_week, 
  work_weeks_per_year=WORK_WEEKS_PER_YEAR, tax_tiers=NZ_TAX_TIERS):
    """
    Return the income tax due and the effective tax rate on the gross yearly income ``gross_hourly_income*hours_per_week*weeks_per_year`` using the given tax tiers.

    EXAMPLES::

        >>> tax_and_rate_h(75, 20)
        (13720.0, 0.19884057971014493)
    """
    gyi = gross_hourly_income*hours_per_week*work_weeks_per_year
    return tax_and_rate(gyi, tax_tiers=tax_tiers)

def gross_yearly_income(net_yearly_income, tax_tiers=NZ_TAX_TIERS):
    """
    Return the gross yearly income required to earn the given   
    net yearly income after subtracting income tax specified by the given 
    tax tiers.
    
    EXAMPLES::
    
        >>> nyi = 50000
        >>> gyi = gross_yearly_income(nyi)
        >>> gyi
        61457.14285714286
        >>> nyi_get = gyi - tax_and_rate(gyi)[0]
        >>> nyi == nyi_get
        True
    """                    
    y = net_yearly_income

    cutoffs, rates = zip(*tax_tiers)
    inverse_cutoffs = [c - tax_and_rate(c)[0] for c in cutoffs]
    k = mindex(y, inverse_cutoffs)
    x = (y + sum([(rates[i] - rates[i + 1])*cutoffs[i] for i in range(k)]))/\
      (1 - rates[k])
    return x

def gross_hourly_income(net_weekly_income, hours_per_week, 
  work_weeks_per_year=WORK_WEEKS_PER_YEAR, tax_tiers=NZ_TAX_TIERS):
    """
    Return the gross hourly income required to earn the given net weekly 
    income for *52* weeks per year when working the given number of hours 
    per week for the given number of weeks per year after subtracting income
    tax specified by the given tax tiers.

    EXAMPLES::

        >>> net_weekly_income = 1200
        >>> hours = 20
        >>> weeks = 47
        >>> ghi = gross_hourly_income(net_weekly_income, hours, weeks) 
        >>> ghi
        84.66179739599875
        >>> gyi = ghi*hours*weeks
        >>> tax, rate = tax_and_rate(gyi)
        >>> nyi = gyi - tax
        >>> net_weekly_income_get = round(nyi/52)
        >>> net_weekly_income == net_weekly_income_get
        True
        >>> rate == tax_and_rate_h(ghi, hours, weeks)[1]
        True
    """    
    gyi = gross_yearly_income(net_weekly_income*52)
    ghi = gyi/(hours_per_week*work_weeks_per_year)
    return ghi

def max_len(items):
    """
    Return the length of the longest item (when converted to a string) 
    in the given list.

    EXAMPLES::

        >>> max_len(['', 'oh', 'boy', 'oh'])
        3
    """
    return max(len(str(item)) for item in items)

def print_table(hours=tuple(5*i for i in range(1, 9)), 
  net_weekly_incomes=tuple(100*i for i in range(1, 26)), 
  weeks=WORK_WEEKS_PER_YEAR, tax_tiers=NZ_TAX_TIERS):
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
    # Create the table
    nwis = net_weekly_incomes
    col_header = [' '] + [str(h) for h in hours]
    table = [['(${!s}, ${!s})'.format(nwi, 52*nwi)] +\
            ['${:.0f}'.format(gross_hourly_income(nwi, hour, weeks, tax_tiers)) 
            for hour in hours] for nwi in net_weekly_incomes]

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
      ------------------------------------------------------
      Gross hourly income given                             
      net (weekly, yearly) income for 52 weeks per year and
      hours worked per week for {!s} weeks per year 
      ------------------------------------------------------""".format(
      weeks, tax_tiers)))

    for i in range(nrows):
        for j in range(ncols):
            print(table[i][j].rjust(col_rjusts[j]), end='')
        print() 

if __name__ == '__main__':
    print_table()