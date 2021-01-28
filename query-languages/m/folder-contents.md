---
description: "Learn more about: Folder.Contents"
title: "Folder.Contents | Microsoft Docs"
ms.date: 10/10/2019
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

Returns a table containing a row for each folder and file found at the folder path, `path`. Each row contains properties of the folder or file and a link to its content.
