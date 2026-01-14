---
description: "Learn more about: Folder.Files"
title: "Folder.Files"
ms.subservice: m-source
ms.topic: reference
---
# Folder.Files

## Syntax

<pre>
Folder.Files(<b>path</b> as text, optional <b>options</b> as nullable record) as table
</pre>

## About

Returns a table containing a row for each file found in the specified folder and all its subfolders.

* `path`: The path to the folder you want to retrieve the files from. The supplied folder path must be a valid absolute path.
* `options`: This parameter is currently intended for internal use only.

Each row of the returned table contains properties of the file and a link to its content.

## Example 1

Return a table containing all of the files found in C:\test-examples\example-folder and all of its subfolders.

**Usage**

```powerquery-m
Folder.Files("C:\test-examples\example-folder")
```

**Output**

A table containing the files, their properties, and a link to their content.
