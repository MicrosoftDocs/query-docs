---
title: "DATESYTD Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.DATESYTD.f1"
helpviewer_keywords: 
  - "DATESYTD function"
ms.assetid: 0e8147d2-e763-454f-aa5d-a706795f7fb7
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# DATESYTD Function (DAX)
Returns a table that contains a column of the dates for the year to date, in the current context.  
  
## Syntax  
  
```  
DATESYTD(<dates> [,<year_end_date>])  
```  
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**dates**|A column that contains dates.|  
|**year_end_date**|(optional) A literal string with a date that defines the year-end date. The default is December 31.|  
  
## Property Value/Return Value  
A table containing a single column of date values.  
  
## Remarks  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column,  
  
-   A table expression that returns a single column of date/time values,  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](../DAX/calculate-function-dax.md).  
  
The **year_end_date** parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'Running Total' for the Internet sales.  
  
To see how this works, create a PivotTable and add the fields, CalendarYear and CalendarQuarter, to the **Row Labels** area of the PivotTable. Then add a measure named **Running Total**, using the formula defined in the code section, to the **Values** area of the PivotTable.  
  
```  
=CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), DATESYTD(DateTime[DateKey]))  
```  
  
## See Also  
[Time Intelligence Functions &#40;DAX&#41;](../DAX/time-intelligence-functions-dax.md)  
[Date and Time Functions &#40;DAX&#41;](../DAX/date-and-time-functions-dax.md)  
[DATESMTD Function &#40;DAX&#41;](../DAX/datesmtd-function-dax.md)  
[DATESQTD Function &#40;DAX&#41;](../DAX/datesqtd-function-dax.md)  
[Get Sample Data](http://go.microsoft.com/fwlink/?LinkId=164474)  
  
