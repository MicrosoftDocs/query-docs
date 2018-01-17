---
title: "Text.Middle | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6b4c37ff-358c-422b-9c11-5dc0b6144bef
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.Middle
Text.Middle(text as nullable text, start as number, optional count as nullable number) as nullable text  
  
## About  
Returns count characters, or through the end of text; at the offset start.  
  
### Example 1  
Find the substring from the text "Hello World" starting at index 6 spanning 5 characters.  
  
```  
Text.Middle("Hello World", 6, 5)  
```  
  
```  
Equals: "World"  
```  
