---
title: "PREVIOUSQUARTER Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.PREVIOUSQUARTER.f1"
helpviewer_keywords: 
  - "PREVIOUSQUARTER function"
ms.assetid: 446f5773-1b67-411f-b65f-d937a41010b0
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# PREVIOUSQUARTER Function (DAX)
Returns a table that contains a column of all dates from the previous quarter, based on the first date in the **dates** column, in the current context.  
  
## Syntax  
  
```  
PREVIOUSQUARTER(<dates>)  
```  
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**dates**|A column containing dates.|  
  
## Return Value  
A table containing a single column of date values.  
  
## Remarks  
This function returns all dates from the previous quarter, using the first date in the input column. For example, if the first date in the **dates** argument refers to June 10, 2009,  this function returns all dates for the quarter January to March, 2009.  
  
The **dates** argument can be any of the following:  
  
-   A reference to a date/time column.  
  
-   A table expression that returns a single column of date/time values.  
  
-   A Boolean expression that defines a single-column table of date/time values.  
  
> [!NOTE]  
> Constraints on Boolean expressions are described in the topic, [CALCULATE Function &#40;DAX&#41;](../DAX/calculate-function-dax.md).  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'previous quarter sales' for Internet sales.  
  
To see how this works, create a PivotTable and add the fields, CalendarYear and CalendarQuarter, to the **Row Labels** area of the PivotTable. Then add a measure, named **Previous Quarter Sales**, using the formula defined in the code section, to the **Values** area of the PivotTable.  
  
```  
=CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), PREVIOUSQUARTER('DateTime'[DateKey]))  
```  
  
## See Also  
[Time Intelligence Functions &#40;DAX&#41;](../DAX/time-intelligence-functions-dax.md)  
[Date and Time Functions &#40;DAX&#41;](../DAX/date-and-time-functions-dax.md)  
[PREVIOUSMONTH Function &#40;DAX&#41;](../DAX/previousmonth-function-dax.md)  
[PREVIOUSDAY Function &#40;DAX&#41;](../DAX/previousday-function-dax.md)  
[PREVIOUSYEAR Function &#40;DAX&#41;](../DAX/previousyear-function-dax.md)  
[Get Sample Data](http://go.microsoft.com/fwlink/?LinkId=164474)  
  
