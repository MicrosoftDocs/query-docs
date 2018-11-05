---
title: "ENDOFQUARTER Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ENDOFQUARTER Function (DAX)
Returns the last date of the quarter in the current context for the specified column of dates.  
  
## Syntax  
  
```dax
ENDOFQUARTER(<dates>)  
```
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**dates**|A column that contains dates.|  
  
## Return Value  
A table containing a single column and single row with a date value.  
  
## Remarks  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column,  
  
-   A table expression that returns a single column of date/time values,  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](calculate-function-dax.md).  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [https://go.microsoft.com/fwlink/?LinkId=219172](https://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that returns the end of the quarter, for the current context.  
  
To see how this works, create a PivotTable and add the fields CalendarYear and MonthNumberOfYear to the **Row Labels** area of the PivotTable. Then add a measure, named **EndOfQuarter**, using the formula defined in the code section, to the **Values** area of the PivotTable.  
  
```dax
=ENDOFQUARTER(DateTime[DateKey])  
```
  
## See Also  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[Time Intelligence Functions &#40;DAX&#41;](time-intelligence-functions-dax.md)  
[ENDOFYEAR Function &#40;DAX&#41;](endofyear-function-dax.md)  
[ENDOFMONTH Function &#40;DAX&#41;](endofmonth-function-dax.md)  
  
