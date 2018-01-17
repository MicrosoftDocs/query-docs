---
title: "Access.Database | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 88702295-2e3c-47f3-993e-a37fee82d9bb
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Access.Database
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
```  
Access.Database(database as binary, optional options as nullable record) as table  
```  
  
## About  
Returns a structural representation of an Access database, <code>database</code>. An optional record parameter, <code>options</code>, may be specified to control the following options: <ul> <li> <code>CreateNavigationProperties</code> : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is false).</li> <li> <code>NavigationPropertyNameGenerator</code> : A function that is used for the creation of names for navigation properties.</li> </ul> The record parameter is specified as [option1 = value1, option2 = value2...] for example.  
  
## Example  
  
```  
Access.Database(File.Contents("c:\users\myuser\Desktop\mydb.accdb"))  
```  
  
