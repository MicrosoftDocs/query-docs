---
title: "Error.Record | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3845be6b-45f3-4060-9fcc-3494b4440bc6
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Error.Record
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a record containing fields ?Reason?, ?Message?, and ?Detail? set to the provided values. The record can be used to raise or throw an error.  
  
```  
Error.Record(reason as text, message as text, detail as any) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|reason|The value to set the Reason as.|  
|message|The value to set the Message as.|  
|detail|The value to set the Detail as.|  
  
## Example  
  
```  
error Error.Record("InvalidCondition","An error has occured", null)  
equals  error with Reason: ?InvalidCondition? and Message ?An error has occurred?  
```  
