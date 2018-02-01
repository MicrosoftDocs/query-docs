---
title: "Folder.Files | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1e287de3-218d-4d9a-938a-34853c15d840
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Folder.Files

  
## About  
Returns a table containing a row for each file found at a folder path, and subfolders. Each row contains properties of the folder or file and a link to its content.  
  
```  
Folder.Files(path as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|path|The path to the folder to retrieve files for.|  
  
