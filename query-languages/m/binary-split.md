---
description: "Learn more about: Binary.Split"
title: "Binary.Split"
---
# Binary.Split

## Syntax

<pre>
Binary.Split(<b>binary</b> as binary, <b>pageSize</b> as number) as list
</pre>

## About

Splits `binary` into a list of binaries where the first element of the output list is a binary containing the first `pageSize` bytes from the source binary, the next element of the output list is a binary containing the next `pageSize` bytes from the source binary, and so on.
