---
title: "Type.FunctionRequiredParameters | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c3269116-7b36-4b66-bad3-b827422a406c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Type.FunctionRequiredParameters
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a number indicating the minimum number of parameters required to invoke the a type of function.  
  
```  
Type.FunctionRequiredParameters(#"type" as type) as number  
```  
  
## Examples  
  
```  
Type.FunctionRequiredParameters( type function () as any) equals 0  
```  
  
```  
Type.FunctionRequiredParameters( type function (x as number) as any) equals 1  
```  
