---
title: "Json.Document | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
---
# Json.Document

  
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
