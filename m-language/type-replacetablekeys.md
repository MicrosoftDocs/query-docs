---
title: "Type.ReplaceTableKeys | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3a35056f-d0bf-4e0d-a686-6808e9e3e73b
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Type.ReplaceTableKeys
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Replaces the keys in a table type.  
  
```  
Type.ReplaceTableKeys(tableType as type,  keys as list) as type  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|tableType|The table type to modify.|  
|keys|The list of keys to replace.|  
  
## Example  
  
```  
Type.ReplaceTableKeys(tableType, {}) equals  returns type value with all keys removed  
```  
