---
description: "Learn more about: Table.PartitionValues"
title: "Table.PartitionValues"
ms.date: 9/13/2021
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.PartitionValues

## Syntax

<pre>
Table.PartitionValues(<b>table</b> as table) as table
</pre>

## About

Returns information about how a table is partitioned. A table is returned where each column is a partition column in the original table, and each row corresponds to a partition in the original table.
