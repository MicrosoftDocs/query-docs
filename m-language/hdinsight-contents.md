---
title: "HdInsight.Contents | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 5d8d8929-3180-4183-a479-ebda8422f4ba
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# HdInsight.Contents
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a navigational table containing all containers found in the HDInsight account. Each row has the container name and table containing its files.  
  
```  
HdInsight.Contents(accountName as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|accountName|The name of the HDInsight account to check.|  
  
