---
description: "Learn more about: HdInsight.Files"
title: "HdInsight.Files | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# HdInsight.Files

## Syntax

<pre>
HdInsight.Files(<b>account</b> as text, <b>containerName</b> as text) as table
</pre>

## About  
Returns a table containing a row for each blob file found at the container URL, `account`, from an Azure storage vault. Each row contains properties of the file and a link to its content.
