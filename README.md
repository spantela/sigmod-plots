# sigmod-plots

[SIGMOD] plot requirements using matplotlib in python.

The user can edit:
  * fonts of the labels, legends, title, x axis and y axis numbers
  * location and size of the image
  * the appearnce of borders
  * the linestyle

The default for the generated image is font 1 requirement and the type is .pdf
in order to allow for flexible resizing in LaTeX files.

To crop the generated pdf to remove any whitespace simply use:

```bash
$ pdfcrop input.pdf output.pdf
```

[SIGMOD]: http://www.sigmod2015.org