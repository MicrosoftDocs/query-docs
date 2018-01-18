---
title: "Date.ToRecord | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a22cb485-4582-451a-b1a1-1f258a2c51c9
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date.ToRecord
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a record containing parts of a Date value.  
  
```  
Date.ToRecord(date as date) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|date|The Date to parse.|  
  
## Example  
  
```  
Date.ToRecord(#date(2013, 1, 1) equals [Year=2013,Month=1,Day=1]  
```  
