---
description: "Learn more about: CLOSINGBALANCEQUARTER"
title: "CLOSINGBALANCEQUARTER function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# CLOSINGBALANCEQUARTER

Evaluates the **expression** at the last date of the quarter in the current context.  
  
## Syntax  
  
```dax
CLOSINGBALANCEQUARTER(<expression>,<dates>[,<filter>])  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|expression|An expression that returns a scalar value.|  
|dates|A column that contains dates.|  
|filter|(optional) An expression that specifies a filter to apply to the current context.|  
  
## Return value

A scalar value that represents the **expression** evaluated at the last date of the quarter in the current context.  
  
## Remarks

- The **dates** argument can be any of the following:  
  
  - A reference to a date/time column.  
  
  - A table expression that returns a single column of date/time values.  
  
  - A Boolean expression that defines a single-column table of date/time values.  
  
    > [!NOTE]  
    > Constraints on Boolean expressions are described in [CALCULATE function](calculate-function-dax.md).  
  
    > [!NOTE]  
    > The **filter** expression has restrictions described in [CALCULATE function](calculate-function-dax.md).  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following sample formula creates a measure that calculates the 'Quarter End Inventory Value' of the product inventory.  
  
```dax
= CLOSINGBALANCEQUARTER(SUMX(ProductInventory,ProductInventory[UnitCost]*ProductInventory[UnitsBalance]),DateTime[DateKey])  
```
  
## See also

[Time intelligence functions](time-intelligence-functions-dax.md)  
[CLOSINGBALANCEYEAR function](closingbalanceyear-function-dax.md)  
[CLOSINGBALANCEMONTH function](closingbalancemonth-function-dax.md)
