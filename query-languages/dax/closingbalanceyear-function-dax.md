---
title: "CLOSINGBALANCEYEAR function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# CLOSINGBALANCEYEAR
Evaluates the **expression** at the last date of the year in the current context.  
  
## Syntax  
  
```dax
CLOSINGBALANCEYEAR(<expression>,<dates>[,<filter>][,<year_end_date>])  
```
  
### Parameters  
  
|||  
|-|-|  
|Parameter|Definition|  
|expression|An expression that returns a scalar value.|  
|dates|A column that contains dates.|  
|filter|(optional) An expression that specifies a filter to apply to the current context.|  
|year_end_date|(optional) A literal string with a date that defines the year-end date. The default is December 31.|  
  
## Return value  
A scalar value that represents the **expression** evaluated at the last date of the year in the current context.  
  
## Remarks  

- The **year_end_date** parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.  

- The **dates** argument can be any of the following:  
  
  - A reference to a date/time column.  
  
  - A table expression that returns a single column of date/time values.  
  
  - A Boolean expression that defines a single-column table of date/time values.  
  
    > [!NOTE]  
    > Constraints on Boolean expressions are described in [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
    > [!NOTE]  
    > The **filter** expression has restrictions described in [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
- This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [https://go.microsoft.com/fwlink/?LinkId=219172](https://go.microsoft.com/fwlink/?LinkId=219172).

## Example

The following sample formula creates a measure that calculates the 'Year End Inventory Value' of the product inventory.  
  
```dax
= CLOSINGBALANCEYEAR(SUMX(ProductInventory,ProductInventory[UnitCost]*ProductInventory[UnitsBalance]),DateTime[DateKey])  
```
  
## See also

[Time-intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[CLOSINGBALANCEYEAR function &#40;DAX&#41;](closingbalanceyear-function-dax.md)  
[CLOSINGBALANCEQUARTER function &#40;DAX&#41;](closingbalancequarter-function-dax.md)  
[CLOSINGBALANCEMONTH function &#40;DAX&#41;](closingbalancemonth-function-dax.md)  
