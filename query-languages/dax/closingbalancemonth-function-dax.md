---
title: "CLOSINGBALANCEMONTH function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/26/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# CLOSINGBALANCEMONTH

Evaluates the **expression** at the last date of the month in the current context.  
  
## Syntax  
  
```dax
CLOSINGBALANCEMONTH(<expression>,<dates>[,<filter>])  
```
  
### Parameters  
  
|Parameter|Definition|  
|-------------|--------------|  
|expression|An expression that returns a scalar value.|  
|dates|A column that contains dates.|  
|filter|(optional) An expression that specifies a filter to apply to the current context.|  
  
## Return value

A scalar value that represents the **expression** evaluated at the last date of the month in the current context.  
  
## Remarks

- The **dates** argument can be any of the following:  
  
  - A reference to a date/time column.  
  
  - A table expression that returns a single column of date/time values.  
  
  - A Boolean expression that defines a single-column table of date/time values.  
  
    > [!NOTE]  
    > Constraints on Boolean expressions are described in [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
    > [!NOTE]  
    > The **filter** expression has restrictions described in [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
- This function is not optimized for use in DirectQuery mode. To learn more, see  [DAX formula compatibility in DirectQuery mode](https://go.microsoft.com/fwlink/?LinkId=219172).
  
## Example

The following sample formula creates a measure that calculates the 'Month End Inventory Value' of the product inventory.  
  
To see how this works, create a PivotTable and add the fields, CalendarYear, MonthNumberOfYear and DayNumberOfMonth, to the **Row Labels** area of the PivotTable. Then add a measure, named **Month End Inventory Value**, using the following formula to the **Values** area of the PivotTable.  
  
```dax
= CLOSINGBALANCEMONTH(SUMX(ProductInventory,ProductInventory[UnitCost]*ProductInventory[UnitsBalance]),DateTime[DateKey])  
```
  
## See also

[Time intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[CLOSINGBALANCEYEAR function &#40;DAX&#41;](closingbalanceyear-function-dax.md)  
[CLOSINGBALANCEQUARTER function &#40;DAX&#41;](closingbalancequarter-function-dax.md)  