---
title: A title
author: Amine Aboufirass
abstract: some abstract
---

::::{ .acronyms }
MD
: Markdown

OOP
: Object Oriented Programming
::::


::::{ .glossary }
function
: An operation which has an input and output

variable
: A symbol which can take on any value in a defined domain
::::

# A header { #sec:my-header }

# Another header

Referencing previous section as Section [sec:my-header]{ .section }

## A subheader

Mentioning a [function]{ .glossary } and a [variable]{ .glossary }.

Mentioning the acronym [OOP]{ .acronyms }, and the acronym [MD]{ .acronyms }.

Mentioning the acronym [OOP]{ .acronyms } a second time, fully abbreviated.

This is some text with *light emphasis*. This is some text with **strong emphasis**.

This is some code `x = 3`.

A block of python code, referenced by Listing [lst:python-code-example]{ .listing }

``` { #lst:python-code-example .python caption="An example of python code" }
def f(x):
    return x**2

if __name__=="__main__":
    x = 3
    y = f(x)
    print(y)
```

A block of .NET code, referenced by Listing [lst:dotnet-code-example]{ .listing }

``` { #lst:dotnet-code-example .cs caption="An example of dotnet code" }
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello");
    }
}
```

An example of a listing imported from an external file. Line [ln:print-statement]{ .line }
contains a `print` statement:

``` {
    #lst:imported-code-block 
    .python 
    firstline=4 
    lastline=8 
    filename=imported-code-block.py
    caption="A block of code imported from an external file"
    }
```

A command line block, without line numbers or highlighting, 

```{
    #lst:command-line-block
    .text
    caption="A command line block"
    linenos="False"
}
PS> get-childitem -recurse .
```

A bulleted list:

- item
    - subitem
    - subitem
    - subitem
- item

An ordered list:

1. item
    1. subitem
    1. subitem
    1. subitem
1. item

A figure, referenced by Figure [fig:banana]{ .figure }

![A banana](banana.jpg){ #fig:banana scale=1.0 }

A simple table, referenced by Table [tab:my-simple-table]{ .table }

:::: {#tab:my-simple-table}
: Simple table caption

  Right     Left     Center     Default
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1
::::

A grid table, referenced by Table [tab:my-grid-table]{ .table }

::::{#tab:my-grid-table}
: Grid table caption

+---------------+---------------+--------------------+
| Fruit         | Price         | Advantages         |
+===============+===============+====================+
| Bananas       |  1.34         | - built-in wrapper |
|               |               | - bright color     |
+---------------+---------------+--------------------+
| Oranges       |  2.10         | - cures scurvy     |
|               |               | - tasty            |
+---------------+---------------+--------------------+
::::

:::: { #tab:my-simple-table-explicit Right=2cm Left=1cm }
: Simple table caption, with explicit column widths

  Right     Left     Center     Default
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1
::::

A `plantuml` class diagram, referenced by Figure [fig:plantuml-diagram]{ .figure }:

``` {#fig:plantuml-diagram .plantuml scale=0.8 caption="A class diagram"}
@startuml

abstract class Beverage {
    description
    getDescription()
    {abstract} cost()
}

class HouseBlend {
    cost()
}

class DarkRoast {
    cost()
}

class Decaf {
    cost()
}

class Espresso {
    cost()
}

Beverage <|-- HouseBlend
Beverage <|-- DarkRoast
Beverage <|-- Decaf
Beverage <|-- Espresso

@enduml
```

A `graphviz` graph, referenced by Figure [fig:graphviz-diagram]{ .figure }.

```{#fig:graphviz-diagram .graphviz caption="A simple flowchart" scale=0.6}
digraph G 
{
    Hello->World
}
```
