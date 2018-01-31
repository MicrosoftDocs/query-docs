---
title: "Text.Insert | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 8bd022f9-de21-4ccb-a467-be6881fb5c0b
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.Insert

  
## About  
Returns a text value with newValue inserted into a text value starting at a zero-based offset.  
  
```  
Text.Insert(text as nullable text, offset as number, newText as text) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to insert into.|  
|offset|The index to insert at.|  
|newText|The new text to insert.|  
  
## <a name="__toc360788855"></a>Remark  
  
-   If offset is less than zero or more than the length of a text value, an Expression.Error is thrown.  
  
## Example  
  
```  
Text.Insert("abcdef",2,"X") equals "abXcdef"  
```  
