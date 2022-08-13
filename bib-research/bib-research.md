---
title: Bibliography research
fontsize: 12pt
header-includes: |
    <style>
    body {
        max-width: 50em;
    }
    </style>
---


- **How to add a lightweight, customizable and complete markdown syntax for including citations 
and bibliography in a markdown file such that conversion with the `panflute` filter will result
in a parseable BibTeX file?**
    - **How does `pandoc` currently convert from one bibliographic format to another?**
        - **How does `pandoc` convert from BibTeX to Markdown?**
        - **How does `pandoc` convert from Markdown to BibTeX?** 
    - **When it performs this conversion, the internal representation is not a `pandoc` AST like 
    the other elements. What is the internal representation?**
        - **Is [CSL](https://docs.citationstyles.org/en/stable/specification.html) (Citation 
        Style Language)  the internal representation?**
            - **What is CSL?**: 
                - *CSL is an XML based format to describe the formatting of 
                citations notes and bibliographies.*
            - **How does CSL work?**
            - **Are CSL YAML and CSL JSON by products of the `pandoc` project or are they
            subsets of CSL XML?**
                - **What is the relationship between CSL XML and CSL YAML?**
                - **What is the relationship between CSL XML and CSL JSON?**
                    - Reference managers make it easy to create a library of items. While many
                    reference managers have their own way of storing item metadata, most
                    support common bibliographic exchange formats such as `BibTeX` and `RIS`.
                    The `citeproc-js` CSL processor introduced a JSON-based format for storing 
                    item metadata in a way `citeproc-js` could understand. Several other CSL 
                    processors have since adopted this "CSL JSON" format (also known as 
                    "citeproc JSON").
                    - **What is a reference manager?**
                        - *A reference manager includes programs like Zotero, Mendeley and Papers
                        which help you automatically generate citations and bibliographies*
                - **Who developed CSL?**
                    - *The Citation Style Language was created by Bruce D'Arcus and shaped
                    by early contributions from Simon Kornblith of Zotero. Frank G. Bennet, Jr
                    and Rintze M. Zelle have spearheaded more recent further development. The
                    CSL `styles` and `locales` GitHub repositories are maintained by Rintze Zelle
                    and Sebastian Karcher.*
                - **Where is the CSL repository?**
                    - *CSL `styles`: [link](https://github.com/citation-style-language/styles)*
                    - *CSL `locales`: [link](https://github.com/citation-style-language/locales)*
                - **What are CSL styles?**
                    - 
                - **What are CSL locales?**
                    - *A file which contains a set of localization data (term translations, 
                    localized date formats, and grammar options, for a particulat language 
                    dialect*
        - **Is there an internal representation?**
