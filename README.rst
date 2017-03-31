Hourly Wage
============
Suppose you work in New Zealand, would like to earn a given net weekly income for 52 weeks per year after income tax, and would like to work a given number of hours per week for 46 weeks per year (*). 
What gross hourly income must you earn?

This little Python 3 program answers that question.::

    ~> python3 hourly_wage.py
    ------------------------------------------------------
    Gross hourly income given                             
    net (weekly, yearly) income for 52 weeks per year and
    hours worked per week for 46 weeks per year 
    ------------------------------------------------------
                         5    10    15    20    25    30    35   40
       ($100, $5200)   $25   $13    $8    $6    $5    $4    $4   $3
      ($200, $10400)   $51   $25   $17   $13   $10    $8    $7   $6
      ($300, $15600)   $77   $39   $26   $19   $15   $13   $11  $10
      ($400, $20800)  $104   $52   $35   $26   $21   $17   $15  $13
      ($500, $26000)  $132   $66   $44   $33   $26   $22   $19  $16
      ($600, $31200)  $159   $80   $53   $40   $32   $27   $23  $20
      ($700, $36400)  $187   $93   $62   $47   $37   $31   $27  $23
      ($800, $41600)  $215  $108   $72   $54   $43   $36   $31  $27
      ($900, $46800)  $247  $124   $82   $62   $49   $41   $35  $31
     ($1000, $52000)  $280  $140   $93   $70   $56   $47   $40  $35
     ($1100, $57200)  $312  $156  $104   $78   $62   $52   $45  $39
     ($1200, $62400)  $346  $173  $115   $87   $69   $58   $49  $43
     ($1300, $67600)  $380  $190  $127   $95   $76   $63   $54  $47
     ($1400, $72800)  $413  $207  $138  $103   $83   $69   $59  $52
     ($1500, $78000)  $447  $224  $149  $112   $89   $75   $64  $56
     ($1600, $83200)  $481  $240  $160  $120   $96   $80   $69  $60
     ($1700, $88400)  $515  $257  $172  $129  $103   $86   $74  $64
     ($1800, $93600)  $548  $274  $183  $137  $110   $91   $78  $69
     ($1900, $98800)  $582  $291  $194  $146  $116   $97   $83  $73
    ($2000, $104000)  $616  $308  $205  $154  $123  $103   $88  $77
    ($2100, $109200)  $650  $325  $217  $162  $130  $108   $93  $81
    ($2200, $114400)  $683  $342  $228  $171  $137  $114   $98  $85
    ($2300, $119600)  $717  $359  $239  $179  $143  $120  $102  $90
    ($2400, $124800)  $751  $375  $250  $188  $150  $125  $107  $94
    ($2500, $130000)  $785  $392  $262  $196  $157  $131  $112  $98

The gross hourly incomes needed are displayed in the body of the table in New Zealand dollars, rounded to the nearest dollar and excluding GST. 
For example, to earn $1200/week after tax, working 25 hours/week, you need to earn $68/hour before tax.

(*) = NZ workers get 4 weeks annual leave plus roughly 2 weeks of public holidays


Authors
========
- Alex Raichev (2014-07)


History
========

v1.0.0, 2017-03-31
-------------------
Removed SciPy dependence


v0.0.0, 2014-07-27
------------------
First release

