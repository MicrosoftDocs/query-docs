---
title: "Table.Unpivot | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 27c2c582-f029-487f-b088-ef4270809fb5
caps.latest.revision: 9
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.Unpivot
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Given a list of table columns, transforms those columns into attribute-value pairs.  
  
```  
Table.Unpivot(table as table, pivotColumns as list, attributeColumn as text, valueColumn as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|pivotColumns|The columns to transform.|  
|attributeColumn|The column to make the attribute.|  
|valueColumn|The column to make the value.|  
  
## <a name="__toc360789588"></a>Remarks  
  
-   The transformation is patterned after the SQL UNPIVOT operator.  
  
## Examples  
  
```  
Table.Unpivot(Table.FromRecords({  
  
    [ key = "key1", attribute1 = 1, attribute2 = null, attribute3 = 3 ]}),  
  
    { "attribute1", "attribute2", "attribute3" }, "attribute", "value")  
```  
  
|key|attribute|value|  
|-------|-------------|---------|  
|key1|attribute1|1|  
|key1|attribute3|3|  
  
