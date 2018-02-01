---
title: "ISEMPTY Function (DAX) | Microsoft Docs"
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
ms.assetid: ded553a5-33b9-4f55-af58-89f370535ad5
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# ISEMPTY Function (DAX)
> [!NOTE]  
> This function is included in SQL Server 2016 Analysis Services (SSAS), Power Pivot in Excel 2016, and Power BI Desktop only. Information provided here is subject to change.  
  
Checks if a table is empty.  
  
## Syntax  
  
```  
ISEMPTY(<table_expression>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table_expression|A table reference or a DAX expression that returns a table.|  
  
## Return Value  
True if the table is empty (has no rows), if else, False.  
  
## Example  
For the below table named ‘Info’:  
  
|Country|State|County|Total|  
|-----------|---------|----------|---------|  
|IND|JK|20|800|  
|IND|MH|25|1000|  
|IND|WB|10|900|  
|USA|CA|5|500|  
|USA|WA|10|900|  
  
```  
EVALUATE   
ROW(“Any countries with count > 25?”, NOT(ISEMPTY(FILTER(Info, [Count]>25)))  
```  
Return value: **FALSE**  
  
