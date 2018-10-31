---
title: "SharePoint.Files | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# SharePoint.Files
`SharePoint.Files(**url** as text, optional **options** as nullable record) as table`

## About

Returns a table containing a row for each document found at the specified SharePoint site, `url`, and subfolders. Each row contains properties of the folder or file and a link to its content. `options` may be specified to control the following options: 

* `ApiVersion` : A number (14 or 15) or the text &quot;Auto&quot; that specifies the SharePoint API version to use for this site. When not specified, API version 14 is used. When Auto is specified, the server version will be automatically discovered if possible, otherwise version defaults to 14. Non-English SharePoint sites require at least version 15.
  
