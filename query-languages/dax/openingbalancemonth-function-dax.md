---
title: "OPENINGBALANCEMONTH function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# OPENINGBALANCEMONTH
Evaluates the **expression** at the first date of the month in the current context.  
  
## Syntax  
  
```dax
OPENINGBALANCEMONTH(<expression>,<dates>[,<filter>])  
```
  
#### Parameters  
  
|||  
|-|-|  
|Parameter|Definition|  
|expression|An expression that returns a scalar value.|  
|dates|A column that contains dates.|  
|filter|(optional) An expression that specifies a filter to apply to the current context.|  
  
## Return value  
A scalar value that represents the **expression** evaluated at the first date of the month in the current context.  
  
## Remarks  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column.  
  
-   A table expression that returns a single column of date/time values.  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
> [!NOTE]  
> The **filter** expression has restrictions described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
>   
> This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [https://go.microsoft.com/fwlink/?LinkId=219172](https://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'Month Start Inventory Value' of the product inventory.  
  
```dax
=OPENINGBALANCEMONTH(SUMX(ProductInventory,ProductInventory[UnitCost]*ProductInventory[UnitsBalance]),DateTime[DateKey])  
```
  
## See also  
[OPENINGBALANCEYEAR function &#40;DAX&#41;](openingbalanceyear-function-dax.md)  
[OPENINGBALANCEQUARTER function &#40;DAX&#41;](openingbalancequarter-function-dax.md)  
[Time-intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[CLOSINGBALANCEMONTH function &#40;DAX&#41;](closingbalancemonth-function-dax.md)  
 
  
