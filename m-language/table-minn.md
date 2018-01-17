---
title: "Table.MinN | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c0a01e40-8abf-4050-99a4-4d9bc1ce9eb4
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.MinN
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the smallest N rows in the given table. After the rows are sorted, the countOrCondition parameter must be specified to further filter the result.  
  
```  
Table.MinN(table as table, comparisonCriteria as any, countOrCondition as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|comparisonCriteria|Smallest N rows comparison criteria.|  
|countOrCondition|After the rows are sorted, countOrCondition further filters the result.|  
  
The **countOrCondition** argument has two possible settings:  
  
|Setting|Description|  
|-----------|---------------|  
|as a number|A list of items up to countOrCondition items in ascending order is returned.|  
|as a condition|A list of items that initially meet the condition is returned. Once an item fails the condition, no further items are considered.|  
  
## Examples  
  
```  
Table.MinN(Employees, "Salary", 3) equals  
```  
  
|Name|Level|Salary|  
|--------|---------|----------|  
|Margo|3|45000|  
|Nikki|5|75000|  
|Andrew|6|85000|  
  
```  
Table.MinN(Employees, "Salary", each [Level] < 6) equals  
```  
  
|Name|Level|Salary|  
|--------|---------|----------|  
|Margo|3|45000|  
|Nikki|5|75000|  
  
