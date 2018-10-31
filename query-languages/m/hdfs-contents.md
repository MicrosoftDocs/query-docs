---
title: "Hdfs.Contents | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Hdfs.Contents

  
## About  
Returns a table containing a row for each folder and file found at the folder **url**, {0}, from a Hadoop file system. Each row contains properties of the folder or file and a link to its content.  
  
## Syntax

<pre> 
Hdfs.Contents(url as text) as table  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|url|The URL to check the contents of.|  
  
