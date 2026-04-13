Use the .venv at the root of this project when running commands

You can import dependencies locally to a function while you are working on it, but after you are done you must
refactor the imports so that they are imported at the top of the file.

While refactoring, don't fallback to the old code unless I tell you to.

Don't do premature optimization. For example, don't cache things unless I ask you to.

When making HTTP requests, start by looking for a helper in the generated and generated_private api directories.

Unless I already specified that something should be optional, assume that when making new functions, every argument is
required.

When implementing code changes, if you start implementing a giant code diff you should stop and run your changes by me first.
I may want to file a ticket to address this later.
