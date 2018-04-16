---
title: "HdInsight.Files | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# HdInsight.Files

  
## About  
Returns a table containing a row for each folder and file found at the container URL, and subfolders from an HDInsight account. Each row contains properties of the file/folder and a link to its content.  
  
```  
HdInsight.Files(accountName as text,  containerName as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|accountName|The name of the HDInsight account to check.|  
|containerName|The name of the table.|  
  
