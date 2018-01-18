---
title: "DATESBETWEEN Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.DATESBETWEEN.f1"
helpviewer_keywords: 
  - "DATESBETWEEN function"
ms.assetid: 74d27354-6aef-4778-9d84-d0f9aeb908ae
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# DATESBETWEEN Function (DAX)
Returns a table that contains a column of dates that begins with the **start_date** and continues until the **end_date**.  
  
## Syntax  
  
```  
DATESBETWEEN(<dates>,<start_date>,<end_date>)  
```  
  
#### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|**dates**|A reference to a date/time column.|  
|**start_date**|A date expression.|  
|**end_date**|A date expression.|  
  
## Return Value  
A table containing a single column of date values.  
  
## Remarks  
If **start_date** is a blank date value, then **start_date** will be the earliest value in the **dates** column.  
  
If **end_date** is a blank date value, then **end_date** will be the latest value in the **dates** column.  
  
The dates used as the **start_date** and **end_date** are inclusive: that is, if the sales occurred on September 1 and you use September 1 as the start date, sales on September 1 are counted.  
  
> [!NOTE]  
> The DATESBETWEEN function is provided for working with custom date ranges. If you are working with common date intervals such as months, quarters, and years, we recommend that you use the appropriate function, such as DATESINPERIOD.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following sample formula creates a measure that calculates the 'Summer 2007 sales' for the Internet sales.  
  
To see how this works, create a PivotTable and add the field, CalendarYear, to the **Row Labels** area of the PivotTable. Then add a measure, named **Summer 2007 Sales**, using the formula as defined in the code section, to the **Values** area of the PivotTable.  
  
```  
=CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), DATESBETWEEN(DateTime[DateKey],  
    DATE(2007,6,1),  
    DATE(2007,8,31)  
  ))  
```  
  
## See Also  
[Time Intelligence Functions &#40;DAX&#41;](../DAX/time-intelligence-functions-dax.md)  
[Date and Time Functions &#40;DAX&#41;](../DAX/date-and-time-functions-dax.md)  
[DATESINPERIOD Function &#40;DAX&#41;](../DAX/datesinperiod-function-dax.md)  
  
