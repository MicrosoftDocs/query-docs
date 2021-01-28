---
description: "Learn more about: LASTDATE"
title: "LASTDATE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# LASTDATE

Returns the last date in the current context for the specified column of dates.  
  
## Syntax  
  
```dax
LASTDATE(<dates>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|dates|A column that contains dates.|  
  
## Return value

A table containing a single column and single row with a date value.  
  
## Remarks

- The **dates** argument can be any of the following:   
  - A reference to a date/time column,  
  - A table expression that returns a single column of date/time values,  
  - A Boolean expression that defines a single-column table of date/time values.  

- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).  
  
- When the current context is a single date, the date returned by the FIRSTDATE and LASTDATE functions will be equal.  
  
- Technically, the Return value is a table that contains a single column and single value. Therefore, this function can be used as an argument to any function that requires a table in its arguments. Also, the returned value can be used whenever a date value is required.  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following sample formula creates a measure that obtains the last date, for the current context, when a sale was made in the Internet sales channel.  
  
To see how this works, create a PivotTable and add the field CalendarYear to the **Row Labels** area of the PivotTable. Then add a measure, named **LastSaleDate**, using the formula defined in the code section, to the **Values** area of the PivotTable.  
  
```dax
= LASTDATE('InternetSales_USD'[SaleDateKey])  
```
  
## See also

[Date and time functions](date-and-time-functions-dax.md)  
[Time intelligence functions](time-intelligence-functions-dax.md)  
[FIRSTDATE function](firstdate-function-dax.md)  
[LASTNONBLANK function](lastnonblank-function-dax.md)
