---
description: "Learn more about: Folder.Files"
title: "Folder.Files"
ms.date: 10/7/2022
---
# Folder.Files

## Syntax

<pre>
Folder.Files(<b>path</b> as text, optional <b>options</b> as nullable record) as table
</pre>

## About

Returns a table containing a row for each file found in the folder `path` and all its subfolders. Each row contains properties of the file and a link to its content. The `options` parameter is currently intended for internal use only.
