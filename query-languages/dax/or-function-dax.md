---
description: "Learn more about: OR"
title: "OR function (DAX) | Microsoft Docs"
---

# OR

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks whether one of the arguments is `TRUE` to return `TRUE`. The function returns `FALSE` if both arguments are `FALSE`.  
  
## Syntax  
  
```dax
OR(<logical1>,<logical2>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`logical_1, logical_2`|The logical values you want to test.|  
  
## Return value

A Boolean value. The value is `TRUE` if any of the two arguments is `TRUE`; the value is FALSE if both the arguments are `FALSE`.  
  
## Remarks

- The `OR` function in DAX accepts only two (2) arguments. If you need to perform an OR operation on multiple expressions, you can create a series of calculations or, better, use the OR operator (**||**) to join all of them in a simpler expression.  
  
- The function evaluates the arguments until the first `TRUE` argument, then returns `TRUE`.  
  
## Example

The following example shows how to use the OR function to obtain the sales people that belong to the Circle of Excellence. The Circle of Excellence recognizes those who have achieved more than a million dollars in Touring Bikes sales or sales of over two and a half million dollars in 2007.  

```dax
IF(   OR(   CALCULATE(SUM('ResellerSales_USD'[SalesAmount_USD]), 'ProductSubcategory'[ProductSubcategoryName]="Touring Bikes") > 1000000  
         ,   CALCULATE(SUM('ResellerSales_USD'[SalesAmount_USD]), 'DateTime'[CalendarYear]=2007) > 2500000  
         )  
   , "Circle of Excellence"  
   , ""  
   )  
```

Returns
  
|Row Labels|2005|2006|2007|2008|-|Grand Total|  
|-------------------|--------|----|----|----|----|----|  
|Abbas, Syed E|||||||  
|Alberts, Amy E|||||||  
|Ansman-Wolfe, Pamela O|||||||  
|Blythe, Michael G|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|  
|Campbell, David R|||||||  
|Carson, Jillian|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|  
|Ito, Shu K|||||||  
|Jiang, Stephen Y|||||||  
|Mensa-Annan, Tete A|||||||  
|Mitchell, Linda C|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|  
|Pak, Jae B|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|  
|Reiter, Tsvi Michael|||||||  
|Saraiva, José Edvaldo|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|  
|Tsoflias, Lynn N|||||||  
|Valdez, Rachel B|||||||  
|Vargas, Garrett R|||||||  
|Varkey Chudukatil, Ranjit R||||||Circle of Excellence|  
|Grand Total|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|Circle of Excellence|  

## Related content

[Logical functions](logical-functions-dax.md)  
