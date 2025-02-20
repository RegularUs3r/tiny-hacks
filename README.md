I usually put here, some hacks/tools/scripts I built or put together in order to help me while pentesting or bug hunting.


## Collection of bash stuff that I usually forgot

##### Vim section
    Remove blank spaces at the end of the line
    :%s/\s\+$//e
    
    Replace backslash with forward slash
    :%s/\\/\//g

    Add stuff at the begining of any string
    :%s!^!!

    Add stuff to the end of any string
    :%s/$/,/
##### Sed section
    Replace blocks of numbers
    sed -E 's/[0-9]+/{something-here}/g'
    
    Remove last char of string
    sed 's/{change-here}$//
    
    Remove/replace char after match
    sed 's/{change-here}.*/ZZZ/g'

    Replace blocks of strings between patterns (e.g =)
    sed -E 's/=([A-Z]+)/{change-here}/g
	
	Remove/Replace up to a point excepts the char after ˆ
	sed 's/string=[ˆ&]//g'

##### jq section
    URL encode
    printf %s "1" | base64 -w0 | jq -sRr @uri

    Find exact match
    jq '.[] | select(.<param>=="<value>")' file
    jq .<param>('value')
    
    Exclude null values
    jq '.[] | select(. != null)'

    Fetch any that starts with
    jq ' .[] | select(. | startswith("<string>"))'

    Extract usefull information from wappalyzer output
    jq ' .technologies | "\(.categories[].name) \(.name) \(.confidence)"'

##### grep section
    extract lines with N digits
    grep -E "[0-9]{4}"

    grep match, but shows everything else
    greo -iz ""

	grep up to a point excepts the char after ˆ
	grep "string=[ˆ&]*"


#### uniqs
    Merge files of line from each
    paste -d "\n" file1 file2 > out

    Sort uniqs by their beginning
    sort -ut '{delimeter-here}' -k1,1 (use it carefully)

#### Powershell
    Find files given a certain extension and get their content
    ForEach ($files in Get-ChildItem -Force -recurse){if ($files -Like "*.txt"){echo $files | Get-Content}}

    Based64 file content encoding
    [convert]::ToBase64String((gc file.txt -Encoding byte))

## Some aliases for good measure

#### Bash Aliases
    #It excludes words with consecutives repeted letter (e.r aaa, bbb and so on)
    nouse='grep -Ev "a{2}|b{2}|c{2}|d{2}|e{2}|f{2}|g{2}|h{2}|i{2}|j{2}|k{2}|l{2}|m{2}|n{2}|o{2}|p{2}|q{2}|r{2}|s{2}|t{2}|u{2}|v{2}|w{2}|x{2}|y{2}|z{2}"'
    
    #Good for filtering junk from waybackruls
    nf='grep -v ".png\|.jpg\|.jpeg\|.svg\|.ttf\|.woff\|.woff2\|.ico\|.eot\|.webp\|.css"'