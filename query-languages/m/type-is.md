---
description: "Learn more about: Type.Is"
title: "Type.Is"
---
# Type.Is

## Syntax

<pre>
Type.Is(<b>type1</b> as type, <b>type2</b> as type) as logical
</pre>

## About

Determines if a value of `type1` is always compatible with `type2`. 

Parameter `type2` is expected to be a nullable primitive type. When this requirement is not met, this function's behavior is undefined and so should not be relied on.

## Example 1

Determine if a value of type number can always also be treated as type any.

**Usage**

```powerquery-m
Type.Is(type number, type any)
```

**Output**

`true`

## Example 2

Determine if a value of type any can always also be treated as type number.

**Usage**

```powerquery-m
Type.Is(type any, type number)
```

**Output**

`false`
