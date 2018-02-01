---
title: "Hdfs.Files | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b792759e-ed69-4f45-8df6-f1e9cd8ab048
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Hdfs.Files

  
## About  
Returns a table containing a row for each file found at the folder **url**, {0}, and subfolders from a Hadoop file system. Each row contains properties of the file and a link to its content.  
  
```  
Hdfs.Files(url as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|url|The URL to check the files of.|  
  
