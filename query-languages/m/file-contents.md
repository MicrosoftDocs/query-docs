---
title: "File.Contents | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
---
# File.Contents

  
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
