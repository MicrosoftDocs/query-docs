---
title: "AzureStorage.Blobs | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 57b5df35-d6c6-42cf-8c22-3c2164fe7562
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# AzureStorage.Blobs
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a navigational table containing all containers found in the Azure Storage account. Each row has the container name and a link to the container blobs.  
  
```  
AzureStorage.Blobs(accountName as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|accountName|The name of the Azure Storage account to access.|  
  
