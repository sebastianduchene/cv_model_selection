library(ape)

dat <- read.dna('150810_WNV.NY99.fasta', format = 'fasta')

split_names <- strsplit(rownames(dat), '[|]')
new_names <- vector()
for(n in 1:length(split_names)){
    temp <- split_names[[n]]
    new_names[n] <- paste0(temp[1], '_', temp[length(temp) - 2 ])
}

rownames(dat) <- new_names
write.dna(dat, file = 'wnv.fasta', format = 'fasta', nbcol = -1, colsep = '')

dat <- dat[, 1:(ncol(dat) - 1)]
dat

for(i in 1:10){
    training_sites <- sample(1:ncol(dat), size = ncol(dat) * 0.8)
    training_data <- dat[, training_sites]
    write.dna(training_data, file = paste0('wnv_training_', i, '.fasta'), format = 'fasta', nbcol = -1, colsep= '')
    test_data <- dat[, -training_sites]
    write.dna(test_data, file = paste0('wnv_test_', i, '.fasta'), format = 'fasta', nbcol = -1, colsep= '')
}


fasta_files <- dir(pattern = 'training.+fasta')

for(f in fasta_files){
    system(paste('../make_xmls.py', f))
}

