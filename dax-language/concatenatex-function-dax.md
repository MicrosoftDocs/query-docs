---
title: "CONCATENATEX Function (DAX) | Microsoft Docs"
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
ms.assetid: cc6ff72f-e9b5-4dbb-977c-276be7effd6a
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# CONCATENATEX Function (DAX)
> [!NOTE]  
> This function is included in SQL Server 2016 Analysis Services (SSAS), Power Pivot in Excel 2016, and Power BI Desktop only. Information provided here is subject to change.  
  
Concatenates the result of an expression evaluated for each row in a table.  
  
## Syntax  
  
```  
CONCATENATEX(<table>, <expression>, [delimiter])  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows for which the expression will be evaluated.|  
|expression|The expression to be evaluated for each row of the table.|  
|delimiter|(optional) A separator to use during concatenation.|  
  
## Return Value  
A text string.  
  
## Remarks  
This function takes as its first argument a table or an expression that returns a table. The second argument is a column that contains the values you want to concatenate, or an expression that returns a value.  
  
## Example  
Employees table  
  
|FirstName|LastName|  
|-------------|------------|  
|Alan|Brewer|  
|Michael|Blythe|  
  
CONCATENATEX(Employees, [FirstName] &amp; “ “ &amp; [LastName], “,”)  
  
Returns "Alan Brewer, Michael Blythe"  
  
