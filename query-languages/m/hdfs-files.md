---
title: "Hdfs.Files | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Hdfs.Files

  
## About  
Returns a table containing a row for each file found at the folder **url**, {0}, and subfolders from a Hadoop file system. Each row contains properties of the file and a link to its content.  
  
## Syntax

<pre>
Hdfs.Files(url as text) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|url|The URL to check the files of.|  
  
