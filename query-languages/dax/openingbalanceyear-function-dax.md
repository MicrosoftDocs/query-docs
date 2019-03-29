---
title: "OPENINGBALANCEYEAR function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# OPENINGBALANCEYEAR
Evaluates the **expression** at the first date of the year in the current context.  
  
## Syntax  
  
```dax
OPENINGBALANCEYEAR(<expression>,<dates>[,<filter>][,<year_end_date>])  
```
  
#### Parameters  
  
|||  
|-|-|  
|Parameter|Definition|  
|expression|An expression that returns a scalar value.|  
|dates|A column that contains dates.|  
|filter|(optional) An expression that specifies a filter to apply to the current context.|  
|year_end_date|(optional) A literal string with a date that defines the year-end date. The default is December 31.|  
  
## Return value  
A scalar value that represents the **expression** evaluated at the first date of the year in the current context.  
  
## Remarks  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column.  
  
-   A table expression that returns a single column of date/time values.  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
> [!NOTE]  
> The **filter** expression has restrictions described in the topic, [CALCULATE function &#40;DAX&#41;](calculate-function-dax.md).  
  
The **year_end_date** parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [https://go.microsoft.com/fwlink/?LinkId=219172](https://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'Year Start Inventory Value' of the product inventory.  
  
To see how this works, create a PivotTable and add the field, CalendarYear, to the **Row Labels** area of the PivotTable. Then add a measure, named **Year Start Inventory Value**, using the formula defined in the code section, to the **Values** area of the PivotTable.  
  
## Code  
  
```dax
=OPENINGBALANCEYEAR(SUMX(ProductInventory,ProductInventory[UnitCost]*ProductInventory[UnitsBalance]),DateTime[DateKey])  
```
  
## See also  
[OPENINGBALANCEQUARTER function &#40;DAX&#41;](openingbalancequarter-function-dax.md)  
[OPENINGBALANCEMONTH function &#40;DAX&#41;](openingbalancemonth-function-dax.md)  
[Time-intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[CLOSINGBALANCEYEAR function &#40;DAX&#41;](closingbalanceyear-function-dax.md)  
 
  
