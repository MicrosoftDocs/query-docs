---
description: "Learn more about: FabricAI.Prompt"
title: "FabricAI.Prompt"
ms.subservice: m-source
---
# FabricAI.Prompt

## Syntax

<pre>
FabricAI.Prompt(<b>input</b> as text, optional <b>context</b> as any) as text
</pre>

## About

Returns the result of passing the specified `input` to an AI model. An optional `context` value can be provided in order to specify additional data that's relevant to the request.

## Example 1

Use an AI model to categorize a product review.

**Usage**

```powerquery-m
FabricAI.Prompt(
    "Categorize the review as positive, negative, or neutral, and extract a single key word in parentheses.",
    [Review = "This is a great product. It only broke four times before we had to return it!"]
)
```

**Output**

`"Negative (broke)"`
