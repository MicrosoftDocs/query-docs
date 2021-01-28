---
description: "Learn more about: AND"
title: "AND function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 01/06/2021
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# AND

Checks whether both arguments are TRUE, and returns TRUE if both arguments are TRUE. Otherwise returns false.  
  
## Syntax  
  
```dax
AND(<logical1>,<logical2>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|logical_1, logical_2|The logical values you want to test.|  
  
## Return value

Returns true or false depending on the combination of values that you test.  
  
## Remarks

The **AND** function in DAX accepts only two (2) arguments. If you need to perform an AND operation on multiple expressions, you can create a series of calculations or, better, use the AND operator (**&&**) to join all of them in a simpler expression.  
  
## Example 1

The following formula shows the syntax of the AND function.  
  
```dax
= IF(AND(10 > 9, -10 < -1), "All true", "One or more false"  
```

Because both conditions, passed as arguments, to the AND function are true, the formula returns "All True".  
  
## Example 2

The following sample uses the AND function with nested formulas to compare two sets of calculations at the same time. For each product category, the formula determines if the current year sales and previous year sales of the Internet channel are larger than the Reseller channel for the same periods. If both conditions are true, for each category the formula returns the value, "Internet hit".  

```dax
= IF( AND(  SUM( 'InternetSales_USD'[SalesAmount_USD])  
           >SUM('ResellerSales_USD'[SalesAmount_USD])  
          , CALCULATE(SUM('InternetSales_USD'[SalesAmount_USD]), PREVIOUSYEAR('DateTime'[DateKey] ))   
           >CALCULATE(SUM('ResellerSales_USD'[SalesAmount_USD]), PREVIOUSYEAR('DateTime'[DateKey] ))  
          )  
     , "Internet Hit"  
     , ""  
     )  
```

Returns
  
|Row Labels|2005|2006|2007|2008|-|Grand Total|  
|----------------|-----------------|----|----|----|----|----|  
|Bib-Shorts|||||||  
|Bike Racks|||||||  
|Bike Stands||||Internet Hit|||  
|Bottles and Cages||||Internet Hit|||  
|Bottom Brackets|||||||  
|Brakes|||||||  
|Caps|||||||  
|Chains|||||||  
|Cleaners|||||||  
|Cranksets|||||||  
|Derailleurs|||||||  
|Fenders||||Internet Hit|||  
|Forks|||||||  
|Gloves|||||||  
|Handlebars|||||||  
|Headsets|||||||  
|Helmets|||||||  
|Hydration Packs|||||||  
|Jerseys|||||||  
|Lights|||||||  
|Locks|||||||  
|Mountain Bikes|||||||  
|Mountain Frames|||||||  
|Panniers|||||||  
|Pedals|||||||  
|Pumps|||||||  
|Road Bikes|||||||  
|Road Frames|||||||  
|Saddles|||||||  
|Shorts|||||||  
|Socks|||||||  
|Tights|||||||  
|Tires and Tubes||||Internet Hit|||  
|Touring Bikes|||||||  
|Touring Frames|||||||  
|Vests|||||||  
|Wheels|||||||  
||||||||  
|Grand Total|||||||  
  
## See also

[Logical functions](logical-functions-dax.md)  
