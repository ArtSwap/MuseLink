# Easy Paray Painter

## Setup guide for use with free GPU compute from Google Colab

![Preview painting](./BeneaththeBlueSky.png)

- Step one: Upload this entire folder to your Google Drive. Don't put it in a subfolder or you'll have to make manual changes to the program to run it.

- Step two: From your Google Drive, open the file EasyPainter.ipynb. This should prompt you to open the notebook in Colab.

- Step three: Double-check that you are using a GPU runtime by clicking the dropdown that says "Runtime", clicking "Change runtime type", and selecting GPU in the dropdown if it is not already selected.

- Step four: The notebook should be run cell-by-cell. Notice the [ ] square brackets by the code cells; hover your mouse over and they turn into a play button. Click the play button to run the cell. Check out https://colab.research.google.com/notebooks/basic_features_overview.ipynb for a more detailed overview of Colab.

- Step five: Simply follow the directions in the notebook. The last two cells can be run repeatedly if you want to try different settings. The outputs should save to your Google Drive by default.

## Notes about licensing

Some of the code, especially the experimental code relating to closed order factorization, was heavily modified from Kim "rosinality" Seonghyeon's stylegan2-pytorch to work with the Paray512 model. The license for that project is included below.

## MIT License

Copyright (c) 2019 Kim Seonghyeon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

___

Arguably enough changes were made that it no longer qualifies as a "substantial portion of the software", but the license is so permissive that it won't hurt to include it. Of course, the "ParayProject" as a whole is unlicensed, all rights are reserved by Paul Paray. Most likely, you're the only one reading this. Replace this paragraph with your own terms as needed, if you plan on any kind of distribution.