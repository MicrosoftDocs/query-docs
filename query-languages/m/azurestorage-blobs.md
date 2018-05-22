---
title: "AzureStorage.Blobs | Microsoft Docs"
ms.date: 5/22/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# AzureStorage.Blobs
<code>AzureStorage.Blobs(<b>account</b> as text, optional <b>options</b> as nullable record) as table</code>
  
## About  

Returns a navigational table containing a row for each container found at the account URL, <code>account</code>, from an Azure storage vault. Each row contains a link to the container blobs.
  
