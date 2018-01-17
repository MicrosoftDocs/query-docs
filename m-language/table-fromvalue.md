---
title: "Table.FromValue | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: d1ba6885-13e6-4ab6-94ef-08d014d262c0
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.FromValue
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table with a column containing the provided value or list of values.  
  
```  
Table.FromValue (value as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|Value|The value to convert.|  
  
## Example  
  
```  
Table.FromValue({1, "Bob", "123-4567"}) equals  
```  
  
|Value|  
|---------|  
|1|  
|Bob|  
|132-4567|  
  
