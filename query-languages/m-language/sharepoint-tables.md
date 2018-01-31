---
title: "SharePoint.Tables | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b60c9f77-1204-4920-adc1-e21b5a21a984
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# SharePoint.Tables
<code>SharePoint.Tables(**url** as text, optional **options** as nullable record) as table</code>

## About

Returns a table containing a row for each List item found at the specified SharePoint list, <code>url</code>. Each row contains properties of the List. <code>options</code> may be specified to control the following options: 

* <code>ApiVersion</code> : A number (14 or 15) or the text &quot;Auto&quot; that specifies the SharePoint API version to use for this site. When not specified, API version 14 is used. When Auto is specified, the server version will be automatically discovered if possible, otherwise version defaults to 14. Non-English SharePoint sites require at least version 15. 
  
