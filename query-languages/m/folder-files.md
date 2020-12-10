---
title: "Folder.Files | Microsoft Docs"
ms.date: 10/10/2019
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan
---
# Folder.Files
  
## Syntax

<pre>
Folder.Files(<b>path</b> as text, optional <b>options</b> as nullable record) as table
</pre>
  
## About

Returns a table containing a row for each file found at the folder path, `path`, and subfolders. Each row contains properties of the file and a link to its content. 
  
