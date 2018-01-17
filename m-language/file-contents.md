---
title: "File.Contents | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 28c835eb-2d89-4b5a-b6c6-048d3811c533
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# File.Contents
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the binary contents of the file located at a path.  
  
```  
File.Contents(path as text) as binary  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|path|The path to the file to retrieve contents for.|  
  
## Example  
  
```  
File.Contents("c:\users\myuser\Desktop\file.txt")  
```  
