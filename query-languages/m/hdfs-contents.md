---
description: "Learn more about: Hdfs.Contents"
title: "Hdfs.Contents | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Hdfs.Contents
  
## Syntax

<pre>
Hdfs.Contents(<b>url</b> as text) as table
</pre> 

## About  
Returns a table containing a row for each folder and file found at the folder URL, `url`, from a Hadoop file system. Each row contains properties of the folder or file and a link to its content.
