# Exercise 02: Copilot Chat

**Aim**: Learn how to use the Copilot Chat to add unit tests. 

## Instructions

Go to the [nightinggale repository](https://github.com/fritjoflammers/nightingale) and create a new codespace by clicking on the green "Code" button and selecting "Open with Codespaces".

In codespaces, open the Chat side panel by clicking on the Github icon on the top right corner of the editor and selecting "Chat" or using the shortcut Ctrl+Alt+I.

As you see this is a R project, which cannot be readily run in codespaces. 

The aim of this exercise is to use CoPilot `Edit`or `Agent` mode to convert it to Python. 

For a start, you can ask CoPilot to only convert the file `R/show_barplot.R`

Tip: You may need to tell it to save the plot to a file, e.g. `barplot.png`, use a specific library like `matplotlib` and multiple iterations until everything works as expected. Note that the input data is modified using R code in the `mortatiltiy.R` file. 