---
title: "HdInsight.Files | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 919250f6-d00e-484b-993b-463485bb6c8e
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
  
