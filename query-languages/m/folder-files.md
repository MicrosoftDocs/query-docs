---
description: "Learn more about: Folder.Files"
title: "Folder.Files | Microsoft Docs"
ms.date: 9/13/2021
ms.service: powerquery
ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo
---
# Folder.Files
  
## Syntax

<pre>
Folder.Files(<b>path</b> as text, optional <b>options</b> as nullable record) as table
</pre>
  
## About

Returns a table containing a row for each file found in the folder `path` and all its subfolders. Each row contains properties of the file and a link to its content. The `options` parameter is currently intended for internal use only.
