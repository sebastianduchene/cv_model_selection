trees <- dir(pattern = '(ucld|exp)[.]trees$')


i = 1

for(i in 2:length(trees)){
    lines <- readLines(trees[i])
    trs <- grep('^tree', lines)
    tr_rm <- trs[1]:trs[length(trs)-1000]
    lines_keep <- lines[-tr_rm]
    writeLines(lines_keep, con = trees[i])
}
