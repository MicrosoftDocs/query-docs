---
title: "Hdfs.Files | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
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
manager: "erikre"
---
# Hdfs.Files
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table containing a row for each file found at the folder **url**, {0}, and subfolders from a Hadoop file system. Each row contains properties of the file and a link to its content.  
  
```  
Hdfs.Files(url as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|url|The URL to check the files of.|  
  
