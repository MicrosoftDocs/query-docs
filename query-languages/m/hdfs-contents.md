---
title: "Hdfs.Contents | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 10a0db2f-14ab-42af-845c-6aec111da60f
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Hdfs.Contents

  
## About  
Returns a table containing a row for each folder and file found at the folder **url**, {0}, from a Hadoop file system. Each row contains properties of the folder or file and a link to its content.  
  
```  
Hdfs.Contents(url as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|url|The URL to check the contents of.|  
  
