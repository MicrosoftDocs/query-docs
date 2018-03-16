---
title: "CALENDARAUTO Function (DAX) | Microsoft Docs"
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
ms.assetid: 54fa359a-3afb-48c3-a437-1c51f30984d4
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# CALENDARAUTO Function (DAX)
> [!NOTE]  
> This function is included in SQL Server 2016 Analysis Services (SSAS), Power Pivot in Excel 2016, and Power BI Desktop only. Information provided here is subject to change.  
  
Returns a table with a single column named “Date” that contains a contiguous set of dates. The range of dates is calculated automatically based on data in the model.  
  
## Syntax  
  
```  
CALENDARAUTO([fiscal_year_end_month])  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|fiscal_year_end_month|Any DAX expression that returns an integer from 1 to 12. If omitted, defaults to the value specified in the calendar table template for the current user, if present; otherwise, defaults to 12.|  
  
## Return Value  
Returns a table with a single column named “Date” that contains a contiguous set of dates. The range of dates is calculated automatically based on data in the model.  
  
## Remarks  
The date range is calculated as follows:  
  
-   The earliest date in the model which is not in a calculated column or calculated table is taken as the MinDate.  
  
-   The latest date in the model which is not in a calculated column or calculated table is taken as the MaxDate.  
  
-   The date range returned is dates between the beginning of the fiscal year associated with MinDate and the end of the fiscal year associated with MaxDate.  
  
An error is returned if the model does not contain any datetime values which are not in calculated columns or calculated tables.  
  
## Example  
In this example, the MinDate and MaxDate in the data model are July 1, 2010 and June 30, 2011.  
  
`CALENDARAUTO()` will return all dates between January 1, 2010 and December 31, 2011.  
  
`CALENDARAUTO(3)` will return all dates between March 1, 2010 and February 28, 2012.  
  
