---
title: "Table.ReplaceKeys | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 54a1517c-5b16-466e-ad44-f239e5c1f37c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.ReplaceKeys
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a new table with new key information set in the **keys** argument.  
  
```  
Table.ReplaceKeys(table as table, keys as list) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|Table to modify.|  
|keys|A list with two fields: Columns and Primary. Columns is a list of columns that are keys. Primary is a primary key.|  
  
## Example  
  
```  
Table.ReplaceKeys(Table.FromRecords({[A={[B=1], [B=2]}, C=1]}), {[Columns = {"C"}, Primary = true]})  
```  
