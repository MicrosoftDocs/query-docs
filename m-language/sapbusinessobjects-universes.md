---
title: "SapBusinessObjects.Universes | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 36c99649-e4c6-4f94-95d9-9878bb89c79b
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# SapBusinessObjects.Universes
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Connects to the SAP BusinessObjects BI Universe at the specified URL and returns the set of available universes.  
  
```  
SapBusinessObjects.Universes(url as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|url|The URL of the SAP BusinessObjects BI Universe to connect to.|  
  
## Remarks  
The function returns a top-level table of two rows. The row with Id = ?Universes? contains a nested table of all of the universes available at the URL. The row with Id = ?DisplayFolders? contains a nested tree of tables representing the display folder hierarchy of the available universes.  
  
The table of universes provides a stable path to access a particular universe by its ID.  
The nested tree of display folder tables provides a user-friendly way to organize and navigate to universes and is not guaranteed to remain stable.  
  
## Examples  
  
```  
SapBusinessObjects.Universes("http://sap.example.com:6405/biprws")  
```  
