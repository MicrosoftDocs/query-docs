---
title: "Value.ReplaceMetadata | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 94b027bd-d2c0-4e1b-9edc-e9523d630784
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Value.ReplaceMetadata
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Replaces the metadata on a value with the new metadata record provided and returns the original value with the new metadata attached.  
  
```  
Value.ReplaceMetadata(value as any, newMeta as record) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value to modify.|  
|newMeta|The new metadata to replace the old metadata with..|  
  
## Example  
  
```  
Value.ReplaceMetadata(1 meta [meta = 1], [meta=2]) equals  1 meta [meta = 2]  
```  
