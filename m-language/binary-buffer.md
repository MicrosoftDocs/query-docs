---
title: "Binary.Buffer | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 86957b53-a352-413c-882a-8f34bf8cb4d0
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Binary.Buffer
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Buffers the binary value in memory. The result of this call is a stable binary value, which means it will have a deterministic length and order of bytes.  
  
```  
Binary.Buffer(binary as nullable binary) as nullable binary  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|Binary|The binary value to buffer in memory.|  
  
