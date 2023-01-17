Melissa Wong
TCSS504 - Minesweeper

This assignment took me about 5.5 hours to complete. It took me longer than
expected to work out how to best tackle this problem. I had initially tried
to create the minefield using nodes, but it ended up being simpler to hold the
data within a 2D array/list.

I first created a solution that didn't account for multiple bombs in a row, but
that obviously failed the second sample test provided in the assignment PDF.
Then when I was able to get my solution to pass the two simpler tests, it ended
up failing the larger tests from official_output.txt. I was able to use the
debugger to work out a simple issue with my if/else statement in the update_row()
method that was preventing the values from incrementing properly.

My solution is pretty verbose, but it's easy to understand, so I'm satisfied
with how it all worked out.