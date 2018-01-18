---
title: "Function.Invoke | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 32840f82-cff0-4a39-9ebb-d6dc3346cdbd
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Function.Invoke
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Invokes the given function using the specified Arguments and returns the result.  
  
```  
Function.Invoke(function as function, args as list) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|function|The function to invoke.|  
|args|The list of required Arguments.|  
  
## Example  
  
```  
Function.Invoke(Record.FieldNames, {[A=1,B=2]}) equals {"A", "B"}  
```  
