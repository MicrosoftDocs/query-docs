---
description: "Learn more about: Hdfs.Files"
title: "Hdfs.Files"
ms.date: 7/29/2019
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Hdfs.Files

## Syntax

<pre>
Hdfs.Files(<b>url</b> as text) as table
</pre>
  
## About  
Returns a table containing a row for each file found at the folder URL, `url`, and subfolders from a Hadoop file system. Each row contains properties of the file and a link to its content.
