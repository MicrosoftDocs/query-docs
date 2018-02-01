---
title: "Text.Start | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b8f50cf2-f671-46a2-9661-75d423d83d63
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.Start

  
## About  
Returns the count of characters from the start of a text value.  
  
```  
Text.Start(string as nullable text, count as number) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The string value to parse.|  
|count|The number of characters to return.|  
  
## Example  
  
```  
Text.Start("abcd", 2) equals "ab"  
```  
