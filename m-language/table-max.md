---
title: "Table.Max | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 05b1e3f6-9a29-4f1b-a4c8-6e23362053ca
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.Max
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the largest row or rows from a table using a comparisonCriteria.  
  
```  
Table.Max(table as table, comparisonCriteria as any, optional default as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|comparisonCriteria|largest row or rows comparison criteria.|  
|optional default|Default value.|  
  
## <a name="__toc360789706"></a>Remarks  
Table.Max is similar to List.Max but requires a table as input.  
  
## Example  
  
```  
Table.Max(Employees, "Salary") equals [Name="Jeff", Level=10, Salary=200000]  
```  
  
|||  
|-|-|  
|Name|Jeff|  
|Level|10|  
|Salary|200000|  
  
