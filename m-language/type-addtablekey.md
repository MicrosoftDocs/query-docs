---
title: "Type.AddTableKey | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 55146283-291d-4ae3-9900-26efa31fc1c3
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Type.AddTableKey
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Add a key to a table type.  
  
```  
Type.AddTableKey (table as type, columns as list,  isPrimary as logical) as type  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The table type to modify.|  
|columns|Columns that define the key.|  
|isPrimary|Logical stating whether or not it is the primary key.|  
  
## Example  
  
```  
Type.AddTableKey(tableType, {"A", "B"}, false) equals  add a non-primary key that combines values from columns A and B  
```  
