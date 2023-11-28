---
description: "Learn more about: OPENINGBALANCEYEAR"
title: "OPENINGBALANCEYEAR function (DAX) | Microsoft Docs"
---
# OPENINGBALANCEYEAR

Evaluates the **expression** at the first date of the year in the current context.  
  
## Syntax  
  
```dax
OPENINGBALANCEYEAR(<expression>,<dates>[,<filter>][,<year_end_date>])  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|expression|An expression that returns a scalar value.|  
|dates|A column that contains dates.|  
|filter|(optional) An expression that specifies a filter to apply to the current context.|  
|year_end_date|(optional) A literal string with a date that defines the year-end date. The default is December 31.|  
  
## Return value

A scalar value that represents the **expression** evaluated at the first date of the year in the current context.  
  
## Remarks

- The **dates** argument can be any of the following:
  - A reference to a date/time column.  
  - A table expression that returns a single column of date/time values.  
  - A Boolean expression that defines a single-column table of date/time values.  
  
- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).  
  
- The **filter** expression has restrictions described in the topic, [CALCULATE function](calculate-function-dax.md).  
  
- The **year_end_date** parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following sample formula creates a measure that calculates the 'Year Start Inventory Value' of the product inventory.  
  
```dax
= OPENINGBALANCEYEAR(SUMX(ProductInventory,ProductInventory[UnitCost]*ProductInventory[UnitsBalance]),DateTime[DateKey])  
```
  
## Related content

[OPENINGBALANCEQUARTER function](openingbalancequarter-function-dax.md)  
[OPENINGBALANCEMONTH function](openingbalancemonth-function-dax.md)  
[Time intelligence functions](time-intelligence-functions-dax.md)  
[CLOSINGBALANCEYEAR function](closingbalanceyear-function-dax.md)  
