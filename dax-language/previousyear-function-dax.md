---
title: "PREVIOUSYEAR Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
f1_keywords: 
  - "sql13.as.daxref.PREVIOUSYEAR.f1"
helpviewer_keywords: 
  - "PREVIOUSYEAR function"
ms.assetid: 94d389d3-5d71-43aa-ba38-c8ff82a2bd8e
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# PREVIOUSYEAR Function (DAX)
Returns a table that contains a column of all dates from the previous year, given the last date in the **dates** column, in the current context.  
  
## Syntax  
  
```  
PREVIOUSYEAR(<dates>[,<year_end_date>])  
```  
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**dates**|A column containing dates.|  
|**year_end_date**|(optional) A literal string with a date that defines the year-end date. The default is December 31.|  
  
## Return Value  
A table containing a single column of date values.  
  
## Remarks  
This function returns all dates from the previous year given the latest date in the input parameter. For example, if the latest date in the **dates** argument refers to the year 2009, then this function returns all dates for the year of 2008, up to the specified **year_end_date**.  
  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column,  
  
-   A table expression that returns a single column of date/time values,  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](../DAX/calculate-function-dax.md).  
  
The **year_end_date** parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the previous year sales for the Internet sales.  
  
To see how this works, create a PivotTable and add the fields, CalendarYear and CalendarQuarter, to the **Row Labels** area of the PivotTable. Then add a measure, named **Previous Year Sales**, using the formula defined in the code section, to the **Values** area of the PivotTable.  
  
```  
=CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), PREVIOUSYEAR('DateTime'[DateKey]))  
```  
  
## See Also  
[Time Intelligence Functions &#40;DAX&#41;](../DAX/time-intelligence-functions-dax.md)  
[Date and Time Functions &#40;DAX&#41;](../DAX/date-and-time-functions-dax.md)  
[PREVIOUSMONTH Function &#40;DAX&#41;](../DAX/previousmonth-function-dax.md)  
[PREVIOUSDAY Function &#40;DAX&#41;](../DAX/previousday-function-dax.md)  
[PREVIOUSQUARTER Function &#40;DAX&#41;](../DAX/previousquarter-function-dax.md)  
  
