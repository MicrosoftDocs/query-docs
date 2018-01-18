---
title: "Type.FunctionParameters | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e22e5ace-c04c-45d0-b3d7-11d516154291
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Type.FunctionParameters
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a record with field values set to the name of the parameters of a function type, and their values set to their corresponding types.  
  
```  
Type.FunctionParameters(functionType as type) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|functionType|The function type to check.|  
  
## Examples  
  
```  
Type.FunctionParameters(type function () as any) equals []  
```  
  
```  
Type.FunctionParameters(type function (x as number, y as text) as any) equals [ x = number, y = text ]  
```  
