---
title: "Json.Document | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: ca2b30f8-e030-4ddf-a97a-f86e52fa16e3
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Json.Document
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the contents of a JSON document.  The contents may be directly passed to the function as text, or it may be the binary value returned by a function like File.Contents.  
  
```  
Json.Document(jsonText as any, optional encoding as nullable number) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|jsonText|Json formatted text.|  
|optional encoding|The encoding value.|  
  
## Example  
  
```  
Json.Document("{""glossary"": { ""title"": ""Example glossary"" } }")    
equals  [glossary = [title = "Example glossary"]]  
```  
