---
description: "Learn more about: HdInsight.Files"
title: "HdInsight.Files"
ms.date: 7/29/2019
---
# HdInsight.Files

## Syntax

<pre>
HdInsight.Files(<b>account</b> as text, <b>containerName</b> as text) as table
</pre>

## About  
Returns a table containing a row for each blob file found at the container URL, `account`, from an Azure storage vault. Each row contains properties of the file and a link to its content.
