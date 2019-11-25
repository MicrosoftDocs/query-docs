---
title: "SharePoint.Tables | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# SharePoint.Tables

## Syntax

<pre>
SharePoint.Tables(<b>url</b> as text, optional <b>options</b> as nullable record) as table
</pre>

## About

Returns a table containing a row for each List item found at the specified SharePoint list, `url`. Each row contains properties of the List. `options` may be specified to control the following options: 

* `ApiVersion` : A number (14 or 15) or the text &quot;Auto&quot; that specifies the SharePoint API version to use for this site. When not specified, API version 14 is used. When Auto is specified, the server version will be automatically discovered if possible, otherwise version defaults to 14. Non-English SharePoint sites require at least version 15. 
  
