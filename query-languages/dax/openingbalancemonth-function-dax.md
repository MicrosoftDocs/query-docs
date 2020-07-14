---
title: "OPENINGBALANCEMONTH function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# OPENINGBALANCEMONTH

Evaluates the **expression** at the first date of the month in the current context.  
  
## Syntax  
  
```dax
OPENINGBALANCEMONTH(<expression>,<dates>[,<filter>])  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|expression|An expression that returns a scalar value.|  
|dates|A column that contains dates.|  
|filter|(optional) An expression that specifies a filter to apply to the current context.|  
  
## Return value

A scalar value that represents the **expression** evaluated at the first date of the month in the current context.  
  
## Remarks

- The **dates** argument can be any of the following:  
  - A reference to a date/time column.  
  - A table expression that returns a single column of date/time values.  
  - A Boolean expression that defines a single-column table of date/time values.  
  
- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).  
  
- The **filter** expression has restrictions described in the topic, [CALCULATE function](calculate-function-dax.md).  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following sample formula creates a measure that calculates the 'Month Start Inventory Value' of the product inventory.  
  
```dax
= OPENINGBALANCEMONTH(SUMX(ProductInventory,ProductInventory[UnitCost]*ProductInventory[UnitsBalance]),DateTime[DateKey])  
```
  
## See also

[OPENINGBALANCEYEAR function](openingbalanceyear-function-dax.md)  
[OPENINGBALANCEQUARTER function](openingbalancequarter-function-dax.md)  
[Time intelligence functions](time-intelligence-functions-dax.md)  
[CLOSINGBALANCEMONTH function](closingbalancemonth-function-dax.md)  
