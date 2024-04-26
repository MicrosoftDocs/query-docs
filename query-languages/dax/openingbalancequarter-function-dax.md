---
description: "Learn more about: OPENINGBALANCEQUARTER"
title: "OPENINGBALANCEQUARTER function (DAX) | Microsoft Docs"
---
# OPENINGBALANCEQUARTER

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Evaluates the **expression** at the first date of the quarter, in the current context.  
  
## Syntax  
  
```dax
OPENINGBALANCEQUARTER(<expression>,<dates>[,<filter>])  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|expression|An expression that returns a scalar value.|  
|dates|A column that contains dates.|  
|filte*|(optional) An expression that specifies a filter to apply to the current context.|  
  
## Return value

A scalar value that represents the **expression** evaluated at the first date of the quarter in the current context.  
  
## Remarks

- The **dates** argument can be any of the following:  
  - A reference to a date/time column.  
  - A table expression that returns a single column of date/time values.
  - A Boolean expression that defines a single-column table of date/time values.  
  
- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).  
  
- The **filter** expression has restrictions described in the topic, [CALCULATE function](calculate-function-dax.md).  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)] 
  
## Example

The following sample formula creates a measure that calculates the 'Quarter Start Inventory Value' of the product inventory.  
  
```dax
= OPENINGBALANCEQUARTER(SUMX(ProductInventory,ProductInventory[UnitCost]*ProductInventory[UnitsBalance]),DateTime[DateKey])  
```
  
## Related content

[OPENINGBALANCEYEAR function](openingbalanceyear-function-dax.md)  
[OPENINGBALANCEMONTH function](openingbalancemonth-function-dax.md)  
[Time intelligence functions](time-intelligence-functions-dax.md)  
[CLOSINGBALANCEQUARTER function](closingbalancequarter-function-dax.md)  
