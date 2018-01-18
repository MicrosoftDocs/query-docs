---
title: "Type.FunctionReturn | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 5d069d1e-0e8c-4b99-a348-78f4825bf550
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Type.FunctionReturn
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a type returned by a function type.  
  
```  
Type.FunctionReturn(type as type) as type  
```  
  
## Examples  
  
```  
Type.FunctionReturn(type function () as any) equals type any  
```  
  
```  
Type.FunctionReturn(type function () as [A = number]) equals type [A = number]  
```  
