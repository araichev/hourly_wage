Hourly Wage
============
Suppose you work in New Zealand, would like to earn a given net weekly income for 52 weeks per year after income tax, and would like to work a given number of hours per week for 47 weeks per year (*). 
What gross hourly income must you earn?

This little Python 3 program answers that question::

    ~> python3 hourly_wage.py
    +-------------------------------------------------------+
    | Gross hourly income given                             |
    | net (weekly, yearly) income for 52 weeks per year and |
    | hours worked per week for 47 weeks per year           |
    +-------------------------------------------------------+
                         5    10    15    20    25    30    35   40
       ($100, $5200)   $24   $12    $8    $6    $4    $4    $3   $3
      ($200, $10400)   $49   $24   $16   $12    $9    $8    $7   $6
      ($300, $15600)   $75   $37   $25   $18   $15   $12   $10   $9
      ($400, $20800)  $102   $51   $34   $25   $20   $17   $14  $12
      ($500, $26000)  $129   $64   $43   $32   $25   $21   $18  $16
      ($600, $31200)  $155   $77   $51   $38   $31   $25   $22  $19
      ($700, $36400)  $182   $91   $60   $45   $36   $30   $26  $22
      ($800, $41600)  $210  $105   $70   $52   $42   $35   $30  $26
      ($900, $46800)  $242  $121   $80   $60   $48   $40   $34  $30
     ($1000, $52000)  $273  $136   $91   $68   $54   $45   $39  $34
     ($1100, $57200)  $305  $152  $101   $76   $61   $50   $43  $38
     ($1200, $62400)  $338  $169  $112   $84   $67   $56   $48  $42
     ($1300, $67600)  $371  $185  $123   $92   $74   $61   $53  $46
     ($1400, $72800)  $404  $202  $134  $101   $80   $67   $57  $50
     ($1500, $78000)  $437  $218  $145  $109   $87   $72   $62  $54
     ($1600, $83200)  $470  $235  $156  $117   $94   $78   $67  $58
     ($1700, $88400)  $503  $251  $167  $125  $100   $83   $71  $62
     ($1800, $93600)  $536  $268  $178  $134  $107   $89   $76  $67
     ($1900, $98800)  $569  $284  $189  $142  $113   $94   $81  $71
    ($2000, $104000)  $602  $301  $200  $150  $120  $100   $86  $75
    ($2100, $109200)  $635  $317  $211  $158  $127  $105   $90  $79
    ($2200, $114400)  $668  $334  $222  $167  $133  $111   $95  $83
    ($2300, $119600)  $701  $350  $233  $175  $140  $116  $100  $87
    ($2400, $124800)  $734  $367  $244  $183  $146  $122  $104  $91
    ($2500, $130000)  $767  $383  $256  $192  $153  $128  $109  $96

The gross hourly incomes needed are displayed in the body of the table in New Zealand dollars, rounded to the nearest dollar and excluding GST. 
For example, to earn $1200/week after tax, working 25 hours/week, you need to earn $68/hour before tax.

(*) NZ workers get 4 weeks annual leave plus roughly 1 week of public holidays

Requires
--------
- Scipy for the root finder scipy.optimize.brentq
