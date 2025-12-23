<!-- TOC -->
# Amazing scripting tool
[Gradle Usage.webm](https://github.com/user-attachments/assets/e6f91cf1-65c0-4528-956c-426894dfc2f1)

<!-- TOC -->
## Requirements
- Bash interpreter(obviously)
- Fortune and cowsay to use the fortune teller
- Rust/Cargo to utilize cargo
- Gradle (ideally 8.14+) and Java (ideally Java 21+) to utilize gradle tools

<!-- TOC -->
## Usage
<p>"main" is the home script from which the rest of the scripts are ran </p>
<p>Adding arguments to main finds directories, if it can't find the directory, it tries to run the argument as a file. </p>
<p>Take this script: </p>

```bash
./main gradle init -o cat
```
<p>It would be the equivelant of: </p>

```bash
./gradle/init -o cat
```
<p>I recommend you add an alias to main to run it anywhere, add this to your .bashrc or .zhsrc file</p>

 ```bash
alias lin="~/BASH_SCRIPTS/main"
```

<p>This way, you can run anything like this: </p>

```bash
lin tell fortune
```
<p>Which would be the equivelant of running this within the BASH_SCRIPTS directory: </p>

```bash

./main tell fortune
```
<!-- TOC -->
# Fun stuff
[Fortune Teller Demo.webm](https://github.com/user-attachments/assets/57eefbab-6c8d-410c-a635-dc9ea988e083)
- You can specify the number of fortunes to tell by tacking on a number as an argument
