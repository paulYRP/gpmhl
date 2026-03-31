---
layout: page
title: Documentation for Developers
description: Guide to update the material on the website for website developers.
permalink: /documentation_developer/
---

# Table of contents

* [How to update the publication page?](#edit_publications)
* [How to update the resource pages?](#edit_resource)

<a id="edit_publications"></a>

## How to update the publication page?

1. The publications are fetched from [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=%28%28%28Mehta%2C+Divya%5BAuthor%5D%29+AND+%28QUT%5BAffiliation%5D%29%29+OR+%28UQ%5BAffiliation%5D%29%29+AND+%28Mehta%2C+Divya%5BAuthor%5D%29&sort=pubdate). Verify that link is working and Divya Mehta is displayed in the content box, next save the results to a summary file by clicking the `Save` button on the top left, and select to save all the abstracts.

   ![](/images/misc/documentation/pubmed.png)

   A file named `abstract-MehtaDivya-set.txt` will be downloaded. Copy this file to `publications/` in this code repository. You can also update the existing abstract file `publications/aabstract-MehtaDivya-set.txt` by simply copy and pasting a new abstract to the beginning of the file.
1. Run the python script to convert the abstracts to a YML file. Under the root directory of this repository, run

   ```
   python publications/pubmed_abstracts_to_yml.py   
   ```

   The output YML file will be in `_data/publications.yml`. The keyword tags are automatically assigned based on the abstract of each article, using the `kwmap` variable in the script `pubmed_abstracts_to_yml.py`.

<a id="edit_resource"></a>

## How to update the resource page?

The resources are currently hard-coded and have to be updated manually. The related data are located in

   ```
   _data/resources/software.yml
   _data/resources/pipelines.yml
   _data/resources/scripts_datasets.yml
   ```

   and the corresponding webpages are located in

   ```
   _pages/software.html
   _pages/pipelines.html
   _pages/scripts_datasets.html
   ```

   Update the YML file (following the existing examples) to update the corresponding webpage.


