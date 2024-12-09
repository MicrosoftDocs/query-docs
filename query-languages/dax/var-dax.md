---
description: "Learn more about: VAR"
title: "VAR keyword (DAX)"
---
# VAR
  
Stores the result of an expression as a named variable, which can then be passed as an argument to other measure expressions. Once resultant values have been calculated for a variable expression, those values do not change, even if the variable is referenced in another expression.  

## Syntax  
  
```dax
VAR <name> = <expression>  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`name`|The name of the variable (identifier).<br />Delimiters are not supported. For example, 'varName' or [varName] will result in an error.<br />Supported character set: a-z, A-Z, 0-9.<br />   0-9 are not valid as first character.<br />__ (double underscore) is allowed as a prefix to the identifier name.<br />No other special characters are supported.<br />Reserved keywords not allowed.<br />Names of existing tables are not allowed.<br />Empty spaces are not allowed.|  
|`expression`|A DAX expression which returns a scalar or table value.|  
  
## Return value

A named variable containing the result of the expression argument.   
  
## Remarks

- An expression passed as an argument to VAR can contain another VAR declaration.  
  
- When referencing a variable:  
  - Measures cannot refer to variables defined outside the measure expression, but can refer to functional scope variables defined within the expression.  
  - Variables can refer to measures.  
  - Variables can refer to previously defined variables.  
  - Columns in table variables cannot be referenced via TableName[ColumnName] syntax.  

- For best practices when using VAR, see [Use variables to improve your DAX formulas](best-practices/dax-variables.md).

- To learn more about how VAR is used within a DAX Query, see [DAX queries](dax-queries.md).

## Example

To calculate a percentage of year-over-year growth without using a variable, you could create three separate measures. This first measure calculates Sum of Sales Amount:  
  
```dax
Sum of SalesAmount = SUM(SalesTable[SalesAmount])  
```

A second measure calculates the sales amount for the previous year:  
  
```dax
SalesAmount PreviousYear =
    CALCULATE([Sum of SalesAmount],
    SAMEPERIODLASTYEAR(Calendar[Date])
    )  
```

You can then create a third measure that combines the other two measures to calculate a growth percentage. Notice the Sum of SalesAmount measure is used in two places; first to determine if there is a sale, then again to calculate a percentage.  
  
```dax
Sum of SalesAmount YoY%: = 
    IF([Sum of SalesAmount] ,  
        DIVIDE(([Sum of SalesAmount] – [SalesAmount PreviousYear]), [Sum of SalesAmount])
    )  
```

By using a variable, you can create a single measure that calculates the same result:  
  
```dax
YoY% =
  VAR Sales = 
      SUM(SalesTable[SalesAmount])  
  VAR SalesLastYear =
      CALCULATE ( SUM ( SalesTable[SalesAmount] ), SAMEPERIODLASTYEAR ( 'Calendar'[Date] ) )

  return if(Sales, DIVIDE(Sales – SalesLastYear, Sales))  
```

By using a variable, you can get the same outcome, but in a more readable way. And because the result of the expression is stored in the variable, the measure's performance can be significantly improved because it doesn't have to be recalculated each time it's used.

## Related content

[Use variables to improve your DAX formulas](best-practices/dax-variables.md)  
[DAX queries](dax-queries.md)
