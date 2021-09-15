---
description: "Learn more about: Folder.Contents"
title: "Folder.Contents | Microsoft Docs"
ms.date: 9/13/2021
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan
---
# Folder.Contents

## Syntax

<pre>
Folder.Contents(<b>path</b> as text, optional <b>options</b> as nullable record) as table
</pre>
  
## About

Returns a table containing a row for each folder and file found in the folder `path`. Each row contains properties of the folder or file and a link to its content. The `options` parameter is currently intended for internal use only.
