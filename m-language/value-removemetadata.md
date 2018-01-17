---
title: "Value.RemoveMetadata | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 519e98bf-6ad2-41ca-b2c9-b4a496de4e44
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Value.RemoveMetadata
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Removes the metadata on the value and returns the original value.  
  
```  
Value.RemoveMetadata(value as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value to remove metadata from.|  
  
## Example  
  
```  
Value.RemoveMetadata(1 meta [meta = 1]) equals 1  
```  
