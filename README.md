# iu-jar

An incremental upgrade tool for jar packages

To install `iu-jar`, use pip:  
`pip install iu-jar`  
then, run with `iujar`  

```
Usage:iujar [option]

 option:

     -h or --help: show help info

     -l target-jar [-o list-file-path]: list table of contents for jar
        target-jar:                 string, path of jar file that need to list
        list-file-path:             string, path of 'list-file' file

     -i old-jar -t new-jar [-n incremental-pkg-name] [-d incremental-pkg-dir] [-f force-path]: generate incremental jar
        old-jar:                    string, path of 'old-jar|list-file' file
        new-jar:                    string, path of new-jar file
        incremental-pkg-name:       string, name of output, default is [old-jar].incremental
        incremental-pkg-dir:        string, dir of output, default is current dir
        force-path:                 regex, match the file path that needs to be forced to update

     -u target-jar -a incremental-pkg [-n new-pkg-name] [-d new-pkg-dir] [-I ignore-path]: update jar from incremental jar
        target-jar:                 string, path of jar file that need to update
        incremental-pkg:            string, path of incremental pkg[from -i generate]
        new-pkg-name:               string, new jar name of output, default is replace target-jar
        new-pkg-dir:                string, dir of output, default is dir of target-jar
        ignore-path:                regex, match the file path that needs to be ignore to update

 example:
     %s -i temp/test.jar -t temp/test_new.jar -d temp.out -f '/BOOT-INF/(classes/*|lib/org\.ileler\..*)|/META-INF/*'
     %s -u temp/test.jar -a temp.out/test.jar.incremental -d temp.out
```
