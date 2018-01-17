---
title: "Hdfs.Contents | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
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
manager: "erikre"
---
# Hdfs.Contents
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table containing a row for each folder and file found at the folder **url**, {0}, from a Hadoop file system. Each row contains properties of the folder or file and a link to its content.  
  
```  
Hdfs.Contents(url as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|url|The URL to check the contents of.|  
  
